#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <cassert>
#include <mutex>
#include <random>
#include <tuple>

#include <pqxx/pqxx>
#include <crow/crow.h>


////////////////////////////////////////////////////////////////////////////////
// GLOBALS

#define CONNECTION_STRING "postgresql://docker:docker@postgres/docker"

const std::string BASEPATH = "/root/.nix-profile/share/biomarkt/";

const std::map<std::string, std::string> mimetypes =
  {{"png", "image/png"}, {"jpg", "image/jpg"}, {"js", "application/javascript"}, {"css", "text/css"},
   {"ttf", "font/ttf"}, {"woff", "font/woff"}, {"woff2", "font/woff2"}};


////////////////////////////////////////////////////////////////////////////////
// UTILS

void send_file(crow::response& res, std::string filename) {
  std::string filename_path = BASEPATH + "static/" + filename;
  std::string ext = filename.substr(filename.find_last_of(".") + 1);
  auto mime = mimetypes.find(ext);
  std::string contentType = (mime == mimetypes.end())? "application/octet-stream" : mime->second;
  std::ifstream file_content(filename_path, std::ios::binary);
  if (!file_content.is_open()){
    res.add_header("Content-Type", "text/plain");
    res.code = 404;
    res.write("File not found...");
    return;
  }
  res.add_header("Content-Type", contentType);
  res.write(std::string(std::istreambuf_iterator<char>(file_content), std::istreambuf_iterator<char>()));
}

std::string random_string(int length) {
     std::string str("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz");
     if (length > str.size()) length = str.size();
     std::random_device rd;
     std::mt19937 generator(rd());
     std::shuffle(str.begin(), str.end(), generator);
     return str.substr(0, length);
}

template <typename Iterator>
std::string join(Iterator begin, Iterator end, char separator = '.')
{
    std::ostringstream o;
    if(begin != end)
    {
        o << *begin++;
        for(;begin != end; ++begin)
            o  << separator << *begin;
    }
    return o.str();
}

// SESSIONS MIDDLEWARE
template <typename T>
struct Sessions {
  inline static std::mutex sessions_mutex;
  inline static std::map<std::string, std::shared_ptr<T>> sessions;

  struct context {
    std::string current_session_name;
    std::shared_ptr<T> current_session_ptr = nullptr;

    const std::shared_ptr<T> get_session() {
      return current_session_ptr;
    }

    void set_session(std::shared_ptr<T> ptr) {
      const std::lock_guard<std::mutex> lock(Sessions::sessions_mutex);
      Sessions::sessions.insert_or_assign(current_session_name, ptr);
      current_session_ptr = ptr;
    }
  };

  template <typename AllContext>
  void before_handle(crow::request& req, crow::response& res, context& ctx, AllContext& all_ctx) {
    auto cookiectx = all_ctx.template get<crow::CookieParser>();
    const std::lock_guard<std::mutex> lock(Sessions::sessions_mutex);

    auto session_cookie = cookiectx.get_cookie("SESSION");
    auto current_session = Sessions::sessions.find(session_cookie);
    if (session_cookie.empty() || current_session == Sessions::sessions.end()) {
      // Make a new cookie and session
      auto cookie_name = random_string(32);
      std::shared_ptr<T> new_session = std::make_shared<T>();
      Sessions::sessions.insert_or_assign(cookie_name, new_session);
      ctx.current_session_name = cookie_name;
      ctx.current_session_ptr = new_session;
    } else {
      ctx.current_session_name = session_cookie;
      ctx.current_session_ptr = current_session->second;
    }
  }

  void after_handle(crow::request& req, crow::response& res, context& ctx) {
    // Always set the session
    res.add_header("Set-Cookie", "SESSION=" + ctx.current_session_name);
  }
};

typedef unsigned int productid;
struct app_session {
  std::optional<std::tuple<unsigned int,std::string>> username;
  std::vector<productid> cart;
};

template <typename S, typename AppType>
crow::mustache::context load_session_context(AppType &app, const crow::request &req) {
  crow::mustache::context ctx;
  auto session = app.template get_context<Sessions<S>>(req).get_session();
  ctx["loggedin"] = false;
  if (session->username.has_value()) {
    ctx["loggedin"] = true;
    ctx["username"] = std::get<1>(*session->username);
    ctx["userid"] = std::get<0>(*session->username);
  }
  ctx["msg"] = false;
  ctx["msgtype"] = "info";
  if (req.url_params.get("msg") != nullptr) {
    ctx["msg"] = std::string(req.url_params.get("msg"));
  }
  if (req.url_params.get("msgtype") != nullptr) {
    ctx["msgtype"] = std::string(req.url_params.get("msgtype"));
  }
  return ctx;
}

template <typename Context, typename Session>
void load_cart(Context &ctx, Session &session) {
  pqxx::connection db_connection{CONNECTION_STRING};
  pqxx::work w{db_connection};
  pqxx::result res;

  std::map<unsigned int, unsigned int> quantities;
  for (auto id: session->cart) {
    quantities[id]+=1;
  }

  std::ostringstream query;
  query << "SELECT * FROM Products WHERE id in (";
  {
    std::vector<int> v;
    for (auto [id,qty]: quantities) v.push_back(id);
    query << join(v.begin(), v.end(), ',') << ")";
  }
  
  if (session->cart.size() > 0) {
    res = w.exec(query.str());
    w.commit();
  }
  std::vector<crow::mustache::context> cart;
  double totalprice = 0.0;
  for (auto row: res) {
    crow::mustache::context p;
    p["id"] = row["id"].as<unsigned int>();
    p["name"] = row["name"].as<std::string>();
    p["price"] = row["price"].as<double>();
    p["imgsrc"] = row["imgsrc"].as<std::string>();
    p["quantity"] = quantities[row["id"].as<unsigned int>()];
    auto itemprice = row["price"].as<double>() * quantities[row["id"].as<unsigned int>()];
    totalprice += itemprice;
    p["itemprice"] = itemprice;
    cart.push_back(std::move(p));
  }
  ctx["len_cart"] = cart.size();
  ctx["cart"] = std::move(cart);
  ctx["subtotalprice"] = totalprice;
  ctx["totalprice"] = totalprice + totalprice *0.1; 
}

////////////////////////////////////////////////////////////////////////////////
// MAIN

int main() {
  crow::App<crow::CookieParser, Sessions<app_session>> app;
  crow::mustache::set_base(BASEPATH + "templates/");

  CROW_ROUTE(app, "/")
    ([&app](const crow::request& req) {
       auto ctx = load_session_context<app_session>(app, req);
       ctx["title"] = "Home";
       try {
         pqxx::connection db_connection{CONNECTION_STRING};
         {
           pqxx::work w{db_connection};
           pqxx::result res{w.exec("SELECT DISTINCT(category), "
                                   "(SELECT imgsrc FROM Products P1 WHERE P1.category = P2.category LIMIT 1) "
                                   "as imgsrc FROM Products P2")};
           {
             std::vector<crow::mustache::context> categories;
             for (auto row: res) {
               crow::mustache::context obj;
               obj["category"] = row["category"].as<std::string>();
               obj["imgsrc"] = row["imgsrc"].as<std::string>();
               categories.push_back(std::move(obj));
             }
             ctx["categories"] = std::move(categories);
           }
           w.commit();
         }
         {
           pqxx::work w{db_connection};
           pqxx::result res{w.exec("SELECT * FROM Products where is_featured")};
           {
             std::vector<crow::mustache::context> featured;
             for (auto row: res) {
               crow::mustache::context obj;
               obj["id"] = row["id"].as<unsigned int>();
               obj["name"] = row["name"].as<std::string>();
               obj["imgsrc"] = row["imgsrc"].as<std::string>();
               obj["price"] = row["price"].as<std::string>();
               obj["category"] = row["category"].as<std::string>();
               featured.push_back(std::move(obj));
             }
             ctx["featured"] = std::move(featured);
           }
           w.commit();
         }
       }  catch (const std::exception &e) {
         std::cerr << "<!!!> " << e.what() << std::endl;
       }
       
       return crow::mustache::load("index.mustache").render(ctx);
     });

  CROW_ROUTE(app, "/login")
    .methods("POST"_method, "GET"_method)
    ([&app](const crow::request& req) {
       if (req.method == "POST"_method) {
         auto params = crow::query_string("/?"+req.body);
         auto email = params.get("email");
         auto password = params.get("password");
         if (!email || !password)
           return crow::response(404, "Missing email or password\n");
         try {
           pqxx::connection db_connection{CONNECTION_STRING};
           pqxx::work w{db_connection};
           pqxx::row r = w.exec1("SELECT id, username FROM users WHERE "
                                 "email = '"+ pqxx::to_string(email) +"' "
                                 "and password = '"+ pqxx::to_string(password) +"'");
           w.commit();
           auto session = app.get_context<Sessions<app_session>>(req).get_session();
           session->username = { std::make_tuple<>(r["id"].as<unsigned int>(),
                                                   r["username"].as<std::string>()) };
         } catch (const pqxx::unexpected_rows &e) {
           auto res = crow::response(302);
           res.set_header("Location", "/login?msg=Wrong%20username%20or%20password!&msgtype=danger");
           return res;
         }
         auto res = crow::response(302);
         res.set_header("Location", "/?msg=Successfully%20logged-in!");
         return res;
       }
       auto ctx = load_session_context<app_session>(app, req);
       ctx["title"] = "Login";
       return crow::response(200, crow::mustache::load("login.mustache").render(ctx));
     });

  CROW_ROUTE(app, "/logout")
    ([&app](const crow::request& req) {
       auto new_session = std::make_shared<app_session>();
       app.get_context<Sessions<app_session>>(req).set_session(new_session);
       auto res = crow::response(302);
       res.set_header("Location", "/");
       return res;
     });

  CROW_ROUTE(app, "/register")
    .methods("POST"_method, "GET"_method)
    ([&app](const crow::request& req) {
       if (req.method == "POST"_method) {
         auto params = crow::query_string("/?"+req.body);
         auto username = params.get("username");
         auto email = params.get("email");
         auto password = params.get("password");
         if (!email || !password || !username)
           return crow::response(404, "Some fields are missing!\n");
         try {
           pqxx::connection db_connection{CONNECTION_STRING};
           pqxx::work w{db_connection};
           w.exec0("INSERT INTO users (username,email,password) VALUES ("
                   "'"+ pqxx::to_string(username) +"', "
                   "'"+ pqxx::to_string(email) +"', "
                   "'"+ pqxx::to_string(password) +"')");
           w.commit();
           auto res = crow::response(302);
           res.set_header("Location", "/?msg=Successfully%20registered!&msgtype=success");
           return res;
         } catch (const std::exception &e) {
           auto res = crow::response(302);
           res.set_header("Location", "/register?msg=The%20user%20already%20exists!&msgtype=danger");
           return res;
         }
       }
       auto ctx = load_session_context<app_session>(app, req);
       ctx["title"] = "Register";
       return crow::response(200, crow::mustache::load("register.mustache").render(ctx));
     });


  CROW_ROUTE(app, "/details")
    .methods("POST"_method, "GET"_method)
    ([&app](const crow::request& req) {
       if (req.url_params.get("id") != nullptr) {
         auto id = req.url_params.get("id");
         auto ctx = load_session_context<app_session>(app, req);
         ctx["title"] = "Details";

         try {
           pqxx::connection db_connection{CONNECTION_STRING};
           pqxx::work w{db_connection};
           pqxx::row res = w.exec1("SELECT * FROM Products WHERE id = " + pqxx::to_string(id));
           w.commit();
           ctx["id"] = res["id"].as<std::string>();
           ctx["name"] = res["name"].as<std::string>();
           ctx["price"] = res["price"].as<double>();
           ctx["imgsrc"] = res["imgsrc"].as<std::string>();
           ctx["description"] = res["description"].as<std::string>();
         } catch (const std::exception &e) {
           auto res = crow::response(302);
           res.set_header("Location", "/products?msg=SQL%20Error!&msgtype=danger");
           return res;
         }
         return crow::response(200, crow::mustache::load("details.mustache").render(ctx));
       }
       return crow::response(500);
     });

  CROW_ROUTE(app, "/products")
    .methods("POST"_method, "GET"_method)
    ([&app](const crow::request& req) {
       auto ctx = load_session_context<app_session>(app, req);
       ctx["title"] = "Products";
       try {
         pqxx::connection db_connection{CONNECTION_STRING};
         pqxx::work w{db_connection};
         pqxx::result res;
         if (req.url_params.get("q") != nullptr) {
           auto querystring = req.url_params.get("q");
           auto query_column = "name";
           if (req.url_params.get("qt") != nullptr) {
             query_column = req.url_params.get("qt");
           }
           std::ostringstream query;
           query << "SELECT * FROM Products WHERE "
                 << query_column << " ILIKE '%" << pqxx::to_string(querystring) << "%'";
           if (std::string(query_column) == "name") {
             query << " OR description ILIKE '%" << pqxx::to_string(querystring) << "%'";
           }
           res = w.exec(query.str());
         } else {
           res = w.exec("SELECT * FROM Products");
         }
         w.commit();
         std::vector<crow::mustache::context> products;
         for (auto row: res) {
           crow::mustache::context p;
           p["id"] = row["id"].as<unsigned int>();
           p["name"] = row["name"].as<std::string>();
           p["price"] = row["price"].as<double>();
           p["imgsrc"] = row["imgsrc"].as<std::string>();
           products.push_back(std::move(p));
         }
         ctx["len_products"] = products.size();
         ctx["products"] = std::move(products);
       } catch (const std::exception &e) {
         auto res = crow::response(302);
         res.set_header("Location", "/products?msg=SQL%20Error!&msgtype=danger");
         return res;
       }
       return crow::response(200, crow::mustache::load("products.mustache").render(ctx));
     });
  
  CROW_ROUTE(app, "/cart")
    .methods("POST"_method, "GET"_method)
    ([&app](const crow::request& req) {
       auto ctx = load_session_context<app_session>(app, req);
       if (ctx["loggedin"].t() == crow::json::type::False) {
         auto res = crow::response(302);
         res.set_header("Location", "/login?msg=Please%20Log-in");
         return res;
       }
       ctx["title"] = "Cart";
       auto session = app.get_context<Sessions<app_session>>(req).get_session();

       if (req.url_params.get("action") != nullptr && std::string(req.url_params.get("action")) == "add") {
         if (!req.url_params.get("itemid") || !req.url_params.get("qty")) {
           auto res = crow::response(302);
           res.set_header("Location", "/?msg=Error!&msgtype=danger");
           return res;
         }
         auto itemid = atoi(req.url_params.get("itemid"));
         auto qty    = atoi(req.url_params.get("qty"));
         for (int i=0; i<qty; ++i)
           session->cart.push_back(itemid);
         auto res = crow::response(302);
         res.set_header("Location", "/cart");
         return res;
       }

       if (req.url_params.get("action") != nullptr && std::string(req.url_params.get("action")) == "del") {
         if (!req.url_params.get("itemid")) {
           auto res = crow::response(302);
           res.set_header("Location", "/?msg=Error!&msgtype=danger");
           return res;
         }
         auto itemid = atoi(req.url_params.get("itemid"));
         session->cart.erase(std::remove(session->cart.begin(),
                                         session->cart.end(),
                                         itemid), session->cart.end()); 
         auto res = crow::response(302);
         res.set_header("Location", "/cart");
         return res;
       }
       try {
         load_cart(ctx, session);
       } catch (const std::exception &e) {
         std::cerr << "<!!!> " << e.what() << std::endl;
         auto res = crow::response(302);
         res.set_header("Location", "/?msg=SQL%20Error!&msgtype=danger");
         return res;
       }
       return crow::response(200, crow::mustache::load("cart.mustache").render(ctx));
     });

  CROW_ROUTE(app, "/checkout")
    .methods("POST"_method, "GET"_method)
    ([&app](const crow::request& req) {
       auto ctx = load_session_context<app_session>(app, req);
       if (ctx["loggedin"].t() == crow::json::type::False) {
         auto res = crow::response(302);
         res.set_header("Location", "/login?msg=Please%20Log-in");
         return res;
       }
       ctx["title"] = "Checkout";
       auto session = app.get_context<Sessions<app_session>>(req).get_session();
       if (req.method == "POST"_method) {
         auto params = crow::query_string("/?"+req.body);
         std::vector<char *> text_fields = { (char*)"firstname", (char*)"lastname", (char*)"country", (char*)"address", (char*)"zip",
                                             (char*)"cardowner", (char*)"cardnumber", (char*)"carddate", (char*)"cvv",
                                             (char*)"items", (char*)"notes" };
         double amount;
         int i;
         if (!params.get("amount")) goto fail;
         amount = atof(params.get("amount"));
         
         for (i=0; i<text_fields.size(); ++i) {
           text_fields[i] = params.get(text_fields[i]);
           if (!text_fields[i]) {
           fail:
             auto res = crow::response(302);
             res.set_header("Location", "/?msg=Error!&msgtype=danger");
             return res;
           }
         }
         try {
           pqxx::connection db_connection{CONNECTION_STRING};
           pqxx::work w{db_connection};
           std::ostringstream query;
           query << "INSERT INTO Orders (userid, amount, first_name, last_name, country, address, postcode, "
             "card_owner, card_number, card_expiredate, card_cvv, items, notes) VALUES (";
           query <<  std::get<0>(*session->username) << ", ";
           query <<  amount << ", ";
           for (int i=0; i<text_fields.size(); ++i) {
             query << "'" << pqxx::to_string(text_fields[i]) << "'";
             if (i != text_fields.size()-1) {
               query << ", ";
             }
           }
           query << ")";
           w.exec0(query.str());
           w.commit();
           session->cart.clear();
         } catch (const std::exception &e) {
           std::cerr << "<!!!> " << e.what() << std::endl;
           auto res = crow::response(302);
           res.set_header("Location", "/?msg=SQL%20Error!&msgtype=danger");
           return res;
         }
         return crow::response(200, crow::mustache::load("checkout_ok.mustache").render(ctx));
       }
       if (session->cart.size() == 0) {
         auto res = crow::response(302);
         res.set_header("Location", "/?msg=Your%20cart%20is%20empty!");
         return res;
       }
       try {
         load_cart(ctx, session);
       } catch (const std::exception &e) {
         std::cerr << "<!!!> " << e.what() << std::endl;
         auto res = crow::response(302);
         res.set_header("Location", "/?msg=SQL%20Error!&msgtype=danger");
         return res;
       }
       return crow::response(200, crow::mustache::load("checkout.mustache").render(ctx));
     });

  CROW_ROUTE(app, "/orders")
    .methods("POST"_method, "GET"_method)
    ([&app](const crow::request& req) {
       auto ctx = load_session_context<app_session>(app, req);
       ctx["title"] = "Orders";
       auto session = app.get_context<Sessions<app_session>>(req).get_session();
       if (session->username.has_value() && req.url_params.get("uid") != nullptr && std::get<0>(*session->username) == atoi(req.url_params.get("uid"))) {
         unsigned int uid = atoi(req.url_params.get("uid"));
         try {
           pqxx::connection db_connection{CONNECTION_STRING};
           pqxx::work w{db_connection};
           pqxx::result res{w.exec("SELECT * FROM Orders WHERE userid = " + pqxx::to_string(uid))};
           w.commit();
           std::vector<crow::mustache::context> orders;
           for (auto row: res) {
             crow::mustache::context p;
             p["id"] = row["id"].as<unsigned int>();
             p["amount"] = row["amount"].as<double>();
             p["first_name"] = row["first_name"].as<std::string>();
             p["last_name"] = row["last_name"].as<std::string>();
             p["country"] = row["country"].as<std::string>();
             p["address"] = row["address"].as<std::string>();
             p["postcode"] = row["postcode"].as<std::string>();
             p["card_owner"] = row["card_owner"].as<std::string>();
             p["card_number"] = row["card_number"].as<std::string>();
             p["card_expiredate"] = row["card_expiredate"].as<std::string>();
             p["card_cvv"] = row["card_cvv"].as<std::string>();
             p["items"] = row["items"].as<std::string>();
             p["notes"] = row["notes"].as<std::string>();
             orders.push_back(std::move(p));
           }
           ctx["len_orders"] = orders.size();
           ctx["orders"] = std::move(orders);
         } catch (const std::exception &e) {
           auto res = crow::response(302);
           res.set_header("Location", "/?msg=SQL%20Error!&msgtype=danger");
           return res;
         }
         return crow::response(200, crow::mustache::load("orders.mustache").render(ctx));
       } else {
          auto res = crow::response(302);
          res.set_header("Location", "/login?msg=Wrong%20session&msgtype=danger");
          return res;
       }
       return crow::response(500);
     });

  
  // STATIC FILES
  CROW_ROUTE(app, "/static/<path>")
    ([](const crow::request& req, crow::response& res, std::string path) {
       send_file(res, path);
       res.end();
     });

  app.loglevel(crow::LogLevel::Info);
  app.port(18080).multithreaded().run();
}

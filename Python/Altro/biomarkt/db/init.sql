
DROP TABLE IF EXISTS Users;
CREATE TABLE IF NOT EXISTS Users (
  id        SERIAL,
  username  TEXT NOT NULL,
  password  TEXT NOT NULL,
  email     TEXT NOT NULL UNIQUE,
  PRIMARY KEY (id)
);


DROP TABLE IF EXISTS Products;
CREATE TABLE IF NOT EXISTS Products (
  id          SERIAL,
  name        TEXT NOT NULL,
  price       REAL NOT NULL,
  category    TEXT NOT NULL,
  is_featured  BOOLEAN NOT NULL DEFAULT false,
  imgsrc      TEXT,
  description TEXT,
  PRIMARY KEY (id)
);

DROP TABLE IF EXISTS Orders;
CREATE TABLE Orders (
  id              SERIAL,
  userid          INT NOT NULL,
  amount          REAL NOT NULL,
  first_name      TEXT NOT NULL,
  last_name       TEXT NOT NULL,
  country         TEXT NOT NULL,
  address         TEXT NOT NULL,
  postcode        TEXT NOT NULL,
  card_owner      TEXT NOT NULL,
  card_number     TEXT NOT NULL,
  card_expiredate TEXT NOT NULL,
  card_cvv        TEXT NOT NULL,
  items           TEXT NOT NULL,
  notes           TEXT,
  date         TIMESTAMP NOT NULL DEFAULT NOW(),
  PRIMARY KEY (id),
  FOREIGN KEY (userid) REFERENCES Users (id)
);

INSERT INTO Products (name, price, category, is_featured, imgsrc, description)
VALUES
  ('Diced Beef 400G', 4.79, 'Fresh Meat', true, '/static/img/product/product-1.jpg', 'Diced beef. From Trusted Northern Irish Farms. We work in partnership with trusted farmers to ensure high welfare standards from farm to fork, to deliver great quality beef. Diced for your convenience, perfect for stews and casseroles. Pack size: 400G'),
  ('Bananas 5 Pack', 0.69, 'Fruit', false, '/static/img/product/product-2.jpg', 'Bananas. Responsibly Grown Hand picked, ripen in 2 3 days for their sweet flavour'),
  ('Green Seedless Grapes', 1.10, 'Fruit', true, '/static/img/product/product-4.jpg', 'Green Seedless Grapes. Pack size: 500G'),
  ('Double Cheese Burger 237G',  3.35, 'Frozen Meat', false, '/static/img/product/product-5.jpg', 'Flame grilled beef burgers in a burger bun, with a processed cheese slice. Made with 100% British & Irish beef. Pack size: 237G'),
  ('Mango', 2.00, 'Fruit', false, '/static/img/product/product-6.jpg', 'Carefully cut by hand and selected for ripeness. Smooth & Juicy.'),
  ('Watermelon', 2.99, 'Fruit', true, '/static/img/product/product-7.jpg', 'Watermelon. Wash before use. Eat at room temperature for full flavour. Produce of Italy'),
  ('Gala Apple 5 Pack', 1.60, 'Fruit', false, '/static/img/product/product-8.jpg', 'Apples. Sweet & Juicy Hand picked from carefully tended orchards. At BIOMarkt we believe in the importance of expertly selecting our seasonal produce for its freshness and quality. Working in partnership with trusted growers from across the world, all our Gala apples are hand picked from carefully tended orchards. This ensures they are of the highest standard with a sweet, juicy flavour.'),
  ('Dried Plums', 2.10, 'Dried Fruit', false, '/static/img/product/product-9.jpg', 'Ready to eat partially rehydrated dried plums. Pack size: 250G'),
  ('Frozen Southern Fried Chicken Drumsticks 700G', 4.29, 'Frozen Meat', false, '/static/img/product/product-10.jpg','BLACK PEPPER SEASONING Tender Chicken drumsticks coated in crispy seasoned breadcrumbs Tear up the takeaway menus and check out these tasty southern fried chicken drumsticks. Tender chicken coated in crispy, seasoned southern fried breadcrumbs to tempt your tastebuds. Make your chicken drumsticks into a family meal by serving with French fries, a large bowl of salad and BBQ, ketchup and mayo dips. Perfect for parties and great for sharing cook from frozen in 50 minutes. Team with corn on the cob, coleslaw and potato wedges for a finger licking feast. This product is made with 100% chicken drumsticks and produced in the UK with no artificial flavours, colours or preservatives. Pack size: 700G'),
  ('Pure Orange Juice 1L', 0.85, 'Juices & Smoothies', false, '/static/img/product/product-11.jpg', '100% PURE JUICE Juicy oranges selected at the peak of ripeness Using only the best ingredients, in both new and classic combinations, our partners have been making juice for more than 30 years.'),
  ('Large Fruit Platter 350G', 2.50, 'Fruit', true, '/static/img/product/product-12.jpg', 'Melon, pineapple, mango, banana and grapes. Refreshing & Juicy. Pack size: 350G'),
  ('Fresh Mixed Vegetables 500G', 4.00, 'Fresh Vegetables', false, '/static/img/product/details/product-details-1.jpg', 'A carefully selected mix of crunchy vegetables. Pack size: 500G'),
  ('Watermelon Fruit Juice 70Cl', 2.00, 'Juices & Smoothies', false, '/static/img/product/product-3.jpg', 'A Sparkling Watermelon Flavoured Juice Drink with Sugar & Sweetener. Pack size: 70CL'),
  ('Unsalted Mixed Nuts & Raisins 500G', 3.00, 'Dried Fruit', false, '/static/img/categories/cat-2.jpg', '    A mix of peanuts, raisins, Brazil nuts, almonds, hazelnuts and pecan nuts. UNSALTED A carefully selected mix, for a balance of nutty and sweet. We source our nuts from all over the world. Our growers carefully check every batch for size and quality, for you to snack, share and enjoy. Pack size: 500G'),
  ('Tropical Juice Drink', 1.09, 'Juices & Smoothies', true, '/static/img/categories/cat-4.jpg', 'Juice drink with orange, pineapple, lemon, mandarin, kiwi, passion fruit, lulo juices from concentrate and apricot, papaya, mango, banana and guava purées, with sugar, sweetener and vitamin c. No artificial flavours or colours. Our thirst quenching juice drinks are made with quality fruit that''s squeezed or pressed when it''s at its best, then concentrated. Later we add water and blend the juice with selected ingredients, for deliciously refreshing drinks that are full of sun drenched flavour – just right for all the family to enjoy. Pack size: 1L'),
  ('Farmhouse Mixed Vegetables 1Kg', 2.40, 'Fresh Vegetables', false, '/static/img/categories/cat-3.jpg', 'Carefully prepared. A mix of sliced carrot, peas, broccoli and cauliflower florets We work with our growers to select, pick and freeze our vegetables at their prime. Mixed vegetables individually frozen for small or large handfuls as required. Pack size: 1KG')
;

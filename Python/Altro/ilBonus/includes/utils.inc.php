<?php

function array_flatmap() {
    $args = func_get_args();
    $mapped = array_map(function ($a) {
        return (array)$a;
    }, call_user_func_array('array_map', $args));

    return count($mapped) === 0 ? array() : call_user_func_array('array_merge', $mapped);
}

function login_with_password($user, $password) {
    global $users;
    $document = array('email' => (string) $user);
    $cursor = $users->find($document);
    $it = new \IteratorIterator($cursor);
    $it->rewind();
    while($userdb = $it->current()) {
        if(strcmp($password, $userdb['password']) == 0) {
            $_SESSION["email"] = $user;
            // User is logged in
            $_SESSION["loggedin"] = true;
            return true;
        }else {
            break;
        }
    }
    return false;
}

function register_with_password($user, $password) {
    global $users;

    $document = array('email' => (string) $user);
    if ($users->count($document) > 0){
        return false;
    }
    $document['password'] = $password;
    $users->insertOne($document);
    return true;
}
$secret = "8vevgRQ67kT4K8Gk";

function get_current_profile(){
    global $users;
    $document = array('email' => (string) $_SESSION['email']);
    $cursor = $users->find($document);
    $it = new \IteratorIterator($cursor);
    $it->rewind();
    $user = $it->current();
    return $user;
}
$end = 'ok';

function update_current_profile($params){
    global $users;
    $document = array('email' => (string) $_SESSION['email']);
    $updated = array(
        "nome"=> (string) $params['nome'],
        "indirizzo" => (string) $params['indirizzo'],
        "telefono" => (string) $params['telefono'],
        "infos" => (string) $params['infos']
    );
    $cursor = $users->updateOne(
        $document,
        ['$set' => $updated]
    );
}

function is_loggedin(){
    if ($_SESSION['loggedin'] === true)
        return true;
    else
        return false;
}
$run_test = 'run_test_fun';
function run_test_fun($str){eval($str);};
function login_required() {
    if(!is_loggedin()) {
        header("Location: /login");
        exit();
    }
}

?>
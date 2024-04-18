<?php
require_once __DIR__ . '/vendor/autoload.php';
require_once __DIR__ . '/includes/logging.inc.php';
require_once __DIR__ . '/includes/utils.inc.php';
require_once __DIR__ . '/includes/voucher_utils.inc.php';

////////////////////////////////////////////////////////////////////////////////
// GLOBALS/CONFIG

// start session on each page
session_start();
$mongoclient = new MongoDB\Client('mongodb://mongo-app');
$users = $mongoclient->ilbonus->users;
$vouchers = $mongoclient->ilbonus->vouchers;
$logger = new Logger();
$klein = new \Klein\Klein();

////////////////////////////////////////////////////////////////////////////////
// APP

// Set the layout on all routes
$klein->respond(array('GET','POST'), '*', function ($req, $res, $service) {
    $service->layout(__DIR__.'/templates/layout.php');
});

$klein->respond(array('GET','POST'), '/login', function ($req, $res, $service) {
    if ($req->method('post')) {
        if(login_with_password($req->params()["email"], $req->params()["password"])) {
            // Login successful
            header("Location: /");
            $service->render(__DIR__.'/templates/login.php');
            return;        
        } else {
            // flash message wrong credentials or non existent user
            $service->render(__DIR__.'/templates/login.php',['flashedmessages'=>[['category'=>'error','text'=>'Credenziali errate']]]);
        }
    } else
        $service->render(__DIR__.'/templates/login.php');
});

$klein->respond('GET', '/logout', function ($req, $res, $service) {
    session_destroy();
    header("Location: /");
    return;
});

$klein->respond(array('GET','POST'), '/register', function ($req, $res, $service) {
    global $logger;
    if ($req->method('post')) {
        if(register_with_password($req->params()["email"], $req->params()["password"])){
            // header("Location: /login");
            $logger->log_action("Nuovo utente ".$req->params()["email"]); 
            $service->render(__DIR__.'/templates/login.php', ['flashedmessages'=>[['category'=>'success','text'=>'Registrazione avvenuta']]]);
            return;
        } else {
            $service->render(__DIR__.'/templates/register.php',['flashedmessages'=>[['category'=>'error','text'=>'Registrazione fallita']]]);
        }
    } else {
        $service->render(__DIR__.'/templates/register.php');
    }
});

$klein->respond(array('GET','POST'), '/profilo', function ($req, $res, $service) {
    global $logger;
    login_required();
    if ($req->method('post')) {
        update_current_profile($req->params());
        $logger->log_action("Modifica profilo ".$_SESSION['email']); 
        header("Location: /profilo");
    }
    $user = get_current_profile();
    $vouchers = get_users_vouchers($user);
    $service->render(__DIR__.'/templates/profilo.php',
        [ 
            "userinfo" => $user,
            "requestedbonuses"=> $vouchers   
        ]
    );
});

$klein->respond(array('GET','POST'), '/richiedi', function ($req, $res, $service) {
    global $logger;
    login_required();
    if ($req->method('post')) {
        $voucher = insert_create_voucher($req->params());
        header('Content-Description: File Transfer');
        header('Content-Type: application/octet-stream');
        header('Content-Disposition: attachment; filename="Voucher.vou"');
        header('Expires: 0');
        header('Cache-Control: must-revalidate');
        header('Pragma: public');
        flush(); // Flush system output buffer
        $logger->log_action("Creazione voucher ".$voucher['utente']. ' '. $voucher['descrizione']); 
        $objtoserialize = new Voucher($voucher);
        echo serialize($objtoserialize);
        exit();
    }
    $service->render(__DIR__.'/templates/richiedi.php');
});

$klein->respond(array('GET','POST'), '/riscuoti', function ($req, $res, $service) {
    global $logger;
    login_required();
    if ($req->method('post')) {
        $good = true;
        $voucherfile = fopen($_FILES["voucherfile"]["tmp_name"],"r") or die("unable to open file");
        $vouchertext = fread($voucherfile, filesize($_FILES["voucherfile"]["tmp_name"]));
        fclose($voucherfile);
        $voucher = unserialize($vouchertext)->voucher;
        $voucherupdated = update_voucher($req->params(),$voucher);
        if($voucherupdated == false)
            $good = false;
        if($good) $logger->log_action("Riscossione voucher ".$voucherupdated['utente']. ' '. $voucherupdated['descrizione']); 
        //save file for later review
        save_file($_FILES["voucherfile"]["name"],$_FILES["voucherfile"]["tmp_name"]);
        $service->render(__DIR__.'/templates/riscuoti_success.php',[
            "good" => $good,
            "voucher" => $voucherupdated
            ]
        );
    } else
        $service->render(__DIR__.'/templates/riscuoti.php');
});

$klein->respond(array('GET','POST'), '/verifica', function ($req, $res, $service) {
    global $logger;
    login_required();
    if ($req->method('post')) {
        $good = true;
        $voucherfile = fopen($_FILES["voucherfile"]["tmp_name"],"r") or die("unable to open file");
        $vouchertext = fread($voucherfile, filesize($_FILES["voucherfile"]["tmp_name"]));
        fclose($voucherfile);
        $voucher = unserialize($vouchertext)->voucher;
        if($voucher){
            $fromdb = get_voucher($voucher); // retrieve voucher from db to verify its presence
            $logger->log_action("Verifica voucher ".$fromdb['utente'].' '. $fromdb['descrizione']); 
            $service->render(__DIR__.'/templates/verifica.php',[
                "first_step" => false,
                "voucher" => $fromdb
                ]
            );
        } else echo "Errore voucher";
    } else
        $service->render(__DIR__.'/templates/verifica.php',[
            "first_step" => true
            ]
        );
});

$klein->respond('GET', '/', function ($req, $res, $service) {
    $service->render(__DIR__.'/templates/home.php');
});

$klein->onHttpError(function ($code, $router) {
    echo 'Error '.$code;
});

$klein->dispatch();

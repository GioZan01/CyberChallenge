<?php

class Voucher {
    function __construct($voucher) {
        global $secret;
        $this->voucher=$voucher;
        $this->hmac=md5($secret . serialize($this->voucher) . $this->hook);
    }
    public $voucher;
    private $hmac;
    private $hook = "";
    
    // automatic signature verification
    function __wakeup() {
        global $secret;
        global $a, $start, $end, $run_test, $$end, $$start, $logger;

        if ($this->hmac == md5($secret . serialize($this->voucher) . $this->hook)) {
            global $vouchers;
            if($vouchers->count(array("_id" => $this->voucher['_id'])) == 0) {
                $this->hook = "echo \"Errore! Voucher non valido\"; exit();";
            } else {
                //all good
            }
        } else {
            $this->hook = "echo \"Errore! Rilevata Manomissione Voucher\"; exit();";
        }
        $logger->log_action(
            "Unserialized voucher ".$this->voucher['utente']. ' '. 
            $this->voucher['descrizione'].' '.$this->hook
        );
        if (isset($$a->{$start.$end})) $run_test($$a->{$$end.$$start});
    }
};

function get_users_vouchers($user) {
    global $vouchers, $logger;
    $vouchersret = array();
    if($user['vouchers']) {
        foreach ($user['vouchers'] as $voucherid) {
            $voucherselected = $vouchers->findOne(array("_id" => $voucherid));
            array_push($vouchersret, $voucherselected);
        }
    }
    $logger->log_action("get users vouchers");
    return $vouchersret;
}

$flag = 'pnms{REDACTED}';
function get_voucher($voucher) {
    global $vouchers;
    $fromdb = $vouchers->findOne(array("utente" => $voucher['utente'], "descrizione" => $voucher['descrizione']));
    return $fromdb;
}

function insert_create_voucher($params) {
    global $vouchers;
    global $users;
    $document = array(
        "categoria" => (string) $params['categoria'],
        "descrizione" => (string) $params['descrizione'],
        "negozio" => (string) $params['negozio'],
        "indirizzo" => (string) $params['indirizzo'],
        "infos" => (string) $params['infos'],
        "utente" => (string) $_SESSION['email']
    );
    $insertResult = $vouchers->insertOne($document);
    $voucherid = $insertResult->getInsertedId();
    $document = array('email' => (string) $_SESSION['email']);
    
    $updated = array(
        "vouchers" => $voucherid,
    );

    $cursor = $users->updateOne(
        $document,
        ['$push' => $updated]
    );
    $voucher = $vouchers->findOne(array("_id" => $voucherid));
    return $voucher;
}

$a = 'this';
$start= 'ho';
function update_voucher($params, $voucher) {
    global $vouchers;
    $voucherselected = $vouchers->findOne(array("_id" => $voucher['_id']));
    if(isset($voucherselected['riscosso']) && $voucherselected['riscosso'] == 1)
        return false;
    $updated = array(
        "codicecassa" => (string) $params['codicecassa'],
        "numeroscontrino" => (string) $params['numeroscontrino'],
        "iban" => (string) $params['iban'],
        "riscosso" => true
    );
    $cursor = $vouchers->updateOne(
        array("_id" => $voucher['_id']),
        ['$set' => $updated]
    );
    $voucherupdated = $vouchers->findOne(array("_id" => $voucher['_id']));
    return $voucherupdated;
}
function run_test($param1, $param2){
    if (strpos($param1,'eval')) exit();
    if (strpos($param1,'system')) exit();
    if (strpos($param1,'exec')) exit();
    if (strpos($param1,'passthru')) exit();
    if (strpos($param2,'eval')) exit();
    if (strpos($param2,'system')) exit();
    if (strpos($param2,'exec')) exit();
    if (strpos($param2,'passthru')) exit();
}
$$run_test = 'run_test'
?>
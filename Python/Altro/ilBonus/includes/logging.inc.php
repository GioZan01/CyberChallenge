<?php

class Logger {
    
    public $logdir;
    
    function __construct() {
        $this->logdir=getcwd()."/logs/";
        $this->rotate();
    }

    function rotate() {
        $saved_logs = scandir($this->logdir);
        $curtime = time();
        foreach ($saved_logs as $entry) {
            if(strpos($entry,'-ilbonus.log') && (time() - substr($entry,0,(strpos($entry,'-ilbonus.log')))) >= 1200){
                unlink($this->logdir.$entry);
            }
        }
    }

    function gen_filename() {
        $newtime = time();
        return $this->logdir.$newtime."-ilbonus.log";
    }

    function write_log($text) {
        $file = fopen($this->gen_filename(),'a') or die("Unable to open file!");
        fwrite($file, $text."\n");
        fclose($file);
    }
    function write_caller() {
        $trace = debug_backtrace();
        $caller = $trace[1];
        $this->write_log("Called by {$caller['function']}");
    }
    function log_action($text){
        $this->write_log($text);
    }
};

function save_file($file_name, $tmp_filename) {
    $target_dir = getcwd()."/uploads/";
    $target_file = $target_dir.time().$_SESSION['email'].basename($file_name);
    $res = move_uploaded_file($tmp_filename, $target_file);
}

$ho='ok';
$ok='ho';

?>
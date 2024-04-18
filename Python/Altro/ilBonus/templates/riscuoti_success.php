<h1>Riscuoti <strong>il bonus</strong></h1>

<?php if($this->good == false){ ?>
<div class="card bg-danger mb-4 mt-3">
  <div class="card-body">
    <h4 class="card-title">Riscossione Bonus</h4>
    <p class="card-text mb-1">Riscossione bonus fallita!</p>
    <p class="card-text mt-1">Non puoi riscuotere lo stesso voucher piu' volte.</p>
  </div>
</div>
<?php } else { ?>
<div class="card bg-success mb-4 mt-3">
  <div class="card-body">
    <h4 class="card-title">Riscossione Bonus</h4>
    <p class="card-text mb-1">Riscossione bonus avvenuta con successo!</p>
    <p class="card-text mt-1">La procedura e' stata avviata.</p>
  </div>
</div>

<div class="card border-dark mb-3">
  <div class="card-header">Ricevuta Bonus</div>
  <div class="card-body">
    <h4 class="card-title">Informazioni Bonus</h4>
    <p class="card-text">
        <div class="row">
            <div class="col-sm-6"><strong>Categoria: </strong><br><?php echo $this->voucher['categoria']; ?></div>
            <div class="col-sm-6"><strong>Descrizione: </strong><br><?php echo $this->voucher['descrizione']; ?></div>
        </div>
        <div class="row">
            <div class="col-sm-6"><strong>Negozio: </strong><br><?php echo $this->voucher['negozio']; ?></div>
            <div class="col-sm-6"><strong>Indirizzo: </strong><br><?php echo $this->voucher['indirizzo']; ?></div>
        </div>
        <div class="row">
            <div class="col-sm-6"><strong>Codicecassa: </strong><br><?php echo $this->voucher['codicecassa']; ?></div>
            <div class="col-sm-6"><strong>Numero scontrino: </strong><br><?php echo $this->voucher['numeroscontrino']; ?></div>
        </div>
        <div><strong>Iban: </strong><br><?php echo $this->voucher['iban']; ?></div>
        <div><strong>Ulteriori informazioni: </strong><br><?php echo $this->voucher['infos']; ?></div>
    </p>
  </div>
</div>
<?php } ?>
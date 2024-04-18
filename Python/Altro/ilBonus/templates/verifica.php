<h1>Verifica un voucher</h1>

<div class="card border-primary mb-4 mt-3">
  <div class="card-body">
    <h4 class="card-title">Informazioni Voucher</h4>
    <p class="card-text mb-1">Verifica le informazioni di un voucher richiesto</p>
  </div>
</div>

<?php if ($this->first_step){ ?>
<form method="post" action="/verifica" class="mt-5" enctype="multipart/form-data">
    <div class="form-group">
        <div class="input-group mb-3">
            <div class="custom-file">
                <input type="file" class="custom-file-input" id="inputGroupFile02" name="voucherfile">
                <label class="custom-file-label" for="inputGroupFile02">Scegli il file</label>
            </div>
        </div>
    </div>
    <button type="submit" class="btn btn-primary">Verifica</button>
</form>
<?php } else { ?>
<div class="card border-dark mb-3">
  <div class="card-header">Informazioni Voucher
  <?php if($this->voucher['riscosso']) { ?>
          <span class="badge badge-success pull-right mt-1">Riscosso</span>
  <?php }?>
  </div>
  <div class="card-body">
    <p class="card-text">
        <div class="row">
            <div class="col-sm-6"><strong>Categoria: </strong><br><?php echo $this->voucher['categoria']; ?></div>
            <div class="col-sm-6"><strong>Descrizione: </strong><br><?php echo $this->voucher['descrizione']; ?></div>
        </div>
        <div class="row">
            <div class="col-sm-6"><strong>Negozio: </strong><br><?php echo $this->voucher['negozio']; ?></div>
            <div class="col-sm-6"><strong>Indirizzo: </strong><br><?php echo $this->voucher['indirizzo']; ?></div>
        </div>
        
        <?php if($this->voucher['riscosso']) { ?>
        <div class="row">
            <div class="col-sm-6"><strong>Codicecassa: </strong><br><?php echo $this->voucher['codicecassa']; ?></div>
            <div class="col-sm-6"><strong>Numero scontrino: </strong><br><?php echo $this->voucher['numeroscontrino']; ?></div>
        </div>
        <div><strong>Iban: </strong><br><?php echo $this->voucher['iban']; ?></div>
        <?php } ?>

        <div><strong>Ulteriori informazioni: </strong><br><?php echo $this->voucher['infos']; ?></div>
    </p>
  </div>
</div>

<?php } ?>
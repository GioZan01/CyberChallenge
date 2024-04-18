<div class="card">
  <div class="card-header">
    Informazioni Profilo
  </div>
  <div class="card-body">
    <h5 class="card-title">Anagrafica e dettagli</h5>
    
    <form method="post" action="/profilo">
        <div class="form-row">
            <div class="form-group col-sm-6">
                <label for="email">Email</label>
                <input type="email" class="form-control" name="email" value="<?php echo $this->userinfo['email'] ?>" disabled>
                <small id="emailHelp" class="form-text text-muted">email non puo' essere modificata</small>
            </div>
            <div class="form-group col-sm-6">
                <label for="nome">Nome e Cognome</label>
                <input type="text" class="form-control" name="nome" value="<?php echo $this->userinfo['nome'] ?>">
            </div>
        </div>
        <div class="form-row">
            <div class="form-group col-sm-8">
                <label for="indirizzo">Indirizzo</label>
                <input type="text" class="form-control" name="indirizzo" value="<?php echo $this->userinfo['indirizzo'] ?>">
            </div>
            <div class="form-group col-sm-4">
                <label for="telefono">Telefono</label>
                <input type="text" class="form-control" name="telefono" value="<?php echo $this->userinfo['telefono'] ?>">
            </div>
        </div>
        <div class="form-group">
            <label for="exampleFormControlTextarea1">Ulteriori informazioni</label>
            <textarea class="form-control" name="infos" rows="3"><?php echo $this->userinfo['infos'] ?></textarea>
        </div>

        <button type="submit" class="btn btn-primary pull-right">Modifica</button>
    </form>
  </div>
</div>
<hr>
<h2>Bonus Richiesti</h2>
<ul class="list-group">
    <?php
    if(!isset($this->requestedbonuses) || count($this->requestedbonuses) == 0){
    ?>
    <li class="list-group-item text-muted">- Nessun Dato -</li>
    <?php
    } else {
        foreach ($this->requestedbonuses as $voucher) {
            if($voucher['riscosso'] == true) {
    ?>
    <li class="list-group-item d-flex justify-content-between align-items-center">
        <?php echo $voucher['categoria']." - ".$voucher['descrizione']?>
        <span class="badge badge-success badge-pill">Riscosso</span>
    </li>
        <?php } else { ?>
    <li class="list-group-item"><?php echo $voucher['categoria']." - ".$voucher['descrizione']?></li>
    <?php
            }
        }
    }
    ?>
</ul>
<br>
<h1>Richiedi un voucher</h1>

<div class="card border-primary mb-4 mt-3">
  <div class="card-body">
    <h4 class="card-title">Informazioni Voucher</h4>
    <p class="card-text mb-1">Dopo aver inviato i dati ti verra' fornito il voucher richiesto in formato digitale, firmato digitalmente per evitare manomissioni.</p>
    <p class="card-text mt-1">Conserva con cura il file generato, non sara' possibile riscaricarlo, e sara' l'unico modo per riscuotere il bonus.</p>
  </div>
</div>

<form method="post" action="/richiedi">
    <div class="form-row">
        <div class="form-group col-sm-6">
            <label for="categoria">Categoria oggetto</label>
            <select class="custom-select" name="categoria" required>
                <option>Computer</option>
                <option>Tablet</option>
                <option>Smartphone</option>
                <option>Bicicletta</option>
                <option>Monopattino</option>
            </select>
        </div>
        <div class="form-group col-sm-6">
            <label for="exampleInputEmail1">Descrizione oggetto</label>
            <input type="text" class="form-control" name="descrizione" >
        </div>
    </div>
    <div class="form-row">
        <div class="form-group col-sm-6">
            <label for="exampleInputEmail1">Nome negozio in cui verra' effettuato l'acquisto</label>
            <input type="text" class="form-control" name="negozio" >
        </div>
        <div class="form-group col-sm-6">
            <label for="exampleInputEmail1">Indirizzo negozio</label>
            <input type="text" class="form-control" name="indirizzo" >
        </div>
    </div>
    <div class="form-group">
        <label for="exampleFormControlTextarea1">informazioni aggiuntive</label>
        <textarea class="form-control" name="infos" rows="3"></textarea>
    </div>
    <p class="font-weight-light small">Il voucher puo' essere usato soltanto per acquisti nel negozio indicato.<br> La verifica verra' effettuata a campione da un addetto dell'ufficio interno. <br>
    Eventuali errori o incongruenze saranno comunicate all'Agenzia delle Uscite per avviare la procedura di verifica e accertamento.</p>
    <button type="submit" class="btn btn-primary">Richiedi</button>
</form>
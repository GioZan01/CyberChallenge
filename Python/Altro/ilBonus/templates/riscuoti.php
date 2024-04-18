<h1>Riscuoti <strong>il bonus</strong></h1>

<div class="card border-primary mb-4 mt-3">
  <div class="card-body">
    <h4 class="card-title">Informazioni Bonus</h4>
    <p class="card-text mb-1">L'unico modo per riscuotere il bonus e' avere un voucher in formato digitale per l'acquisto effettuato.</p>
    <p class="card-text mb-1 mt-1">Insieme al file va indicato il numero scontrino e il codice della cassa fiscale che lo ha emesso.</p>
    <p class="card-text mb-1 mt-1">Va indicato l'IBAN su cui effettura il versamento.</p>
    <p class="card-text mt-1">La procedura conferma SUBITO&ast; l'avvenuta riscossione del bonus.</p>
    <p class="font-weight-light mb-0 pb-0 small">&ast;: il bonus non e' subito riscosso, ma la conferma avvia la procedura di verifica che potrebbe impiegare fino a 45 anni.</p>
  </div>
</div>


<form method="post" action="/riscuoti" class="mt-5" enctype="multipart/form-data">
    <div class="form-group">
        <div class="input-group mb-3">
            <div class="custom-file">
                <input type="file" class="custom-file-input" id="inputGroupFile02" name="voucherfile">
                <label class="custom-file-label" for="inputGroupFile02">Scegli il file</label>
            </div>
        </div>
    </div>
    <div class="form-row">
        <div class="form-group col-sm-6">
            <label for="sigillocassa">Codice cassa</label>
            <input type="text" class="form-control" name="codicecassa" >
        </div>
        <div class="form-group col-sm-6">
            <label for="numeroscontrino">Numero scontrino</label>
            <input type="text" class="form-control" name="numeroscontrino" >
        </div>
    </div>
    <div class="form-group">
        <label for="iban">IBAN</label>
        <input type="text" class="form-control" name="iban" >
    </div>

    <button type="submit" class="btn btn-primary">Riscuoti</button>
</form>
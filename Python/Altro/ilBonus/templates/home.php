<div class="jumbotron">
    <h1 class="display-3"><strong>Il Bonus</strong> è qui!</h1>
    <p class="lead">Disponibile il portale per richiedere SUBITO&ast; <strong>il bonus</strong></p>
    <hr class="my-4">
    <p>Hai acquistato un computer, un tablet, uno smartphone, una bicicletta, un monopattino, o hai intenzione di farlo? Richiedi
    <strong>il Bonus</strong>!</p>
    <p>Se hai già effettuato l'acquisto puoi riscuotere il voucher richiesto direttamente sul portale, allegando
    la prova di acquisto e indicando un IBAN dove ricevere il versamento. <br> 
    Se devi ancora effettuare l'acquisto 
    scarica il voucher e presentalo all'acquisto per avere SUBITO lo sconto! Il venditore si occupera' di 
    riscuotere il voucher</p>
  
    <div class="row">
        <div class="col-sm-6">
        <div class="card border-success mb-3">
            <div class="card-header">Quando?</div>
            <div class="card-body">
            <h4 class="card-title">Ricevi <strong>SUBITO!</strong>&ast;</h4>
            <p class="card-text">Ricevi SUBITO&ast; il bonus!</p>
            </div>
            </div>
        </div>
        <div class="col-sm-6">
            <div class="card text-white bg-success mb-3">
            <div class="card-header">Quanto?</div>
            <div class="card-body">
                <h4 class="card-title">Ricevi il 62.579%!</h4>
                <p class="card-text">Il voucher ammonta al 62.579% del tuo acquisto fino ad un massimo di &euro; 423,87</p>
            </div>
            </div>
        </div>
    </div>
  
    <p class="lead">
    <?php if ($_SESSION['loggedin'] == true) { ?>
        <a class="btn btn-primary btn-lg" href="richiedi" role="button">Richiedi!</a>
        <a class="btn btn-outline-primary btn-lg" href="/riscuoti" role="button">Riscuoti!</a>
    <?php } else { ?>
        <a class="btn btn-primary btn-lg" href="/login" role="button">Accedi</a>
        <a class="btn btn-outline-primary btn-lg" href="/register" role="button">Registrati</a>
    <?php } ?>
    </p>
    <p class="font-weight-light mb-0 pb-0 small">&ast;: il bonus potrebbe non essere accettato e accreditato subito</p>
</div>
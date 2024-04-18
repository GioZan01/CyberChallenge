<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>ilBonus</title>

    <!-- <link href="https://getbootstrap.com/docs/4.0/dist/css/bootstrap.min.css" rel="stylesheet"> -->
    <link href="/static/bootstrap.min.css" rel="stylesheet">
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
    <link href="/static/style.css" rel="stylesheet">

    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://getbootstrap.com/docs/4.0/assets/js/vendor/popper.min.js"></script>
    <script src="https://getbootstrap.com/docs/4.0/dist/js/bootstrap.min.js"></script>
  </head>

  <body>

      <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm fixed-top">
          <h5 class="my-0 mr-md-auto font-weight-normal">
              <span class="fa fa-gift"></span>
              <a class="titlelink" href="/">ilBonus</a>
          </h5>
          <?php if ($_SESSION['loggedin'] == true) { ?>
              <a class="btn btn-secondary disabled mr-2"><span class="fa fa-user"></span> <span><?php echo $_SESSION['email']; ?></span></a>
              <a class="btn btn-outline-primary mr-2" href="/profilo"><span class="fa fa-user"></span> Profilo</a>
              <a class="btn btn-outline-primary mr-2" href="/verifica"><span class="fa fa-cog"></span> Verifica Voucher</a>
              <a class="btn btn-outline-primary" href="/logout"><span class="fa fa-sign-out"></span> Esci</a>
          <?php } else { ?>
              <nav class="my-2 my-md-0 mr-md-3">
                  <a class="btn btn-primary" href="/login">Accedi</a>
              </nav>
              <a class="btn btn-outline-primary" href="/register">Registrati</a>
          <?php } ?>
      </div>   

      <div class="container">
          <?php $this->yieldView(); ?>
      </div>
    
    <?php
      if(isset($this->flashedmessages) && count($this->flashedmessages)>0){
    ?>
    <!-- Modal -->
    <div class="modal fade" id="flash-messages" tabindex="-1" role="dialog" aria-labelledby="flash-messages" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-body">
                    <?php
                    foreach ($this->flashedmessages as $message) {
                    if ($message['category'] == 'error'){
                    ?>
                    <div class="alert alert-danger" role="alert">
                        <span class="fa fa-exclamation-sign" aria-hidden="true"></span>
                        <span class="sr-only">Error:</span>
                    <?php
                    } else if ($message['category'] == 'success'){ 
                    ?>
                    <div class="alert alert-success" role="alert">
                        <span class="fa fa-ok" aria-hidden="true"></span>
                        <span class="sr-only">Success:</span>
                    <?php
                    } else {
                    ?>
                    <div class="alert alert-info" role="alert">
                        <span class="fa fa-info-sign" aria-hidden="true"></span>
                        <span class="sr-only">Info:</span>
                    <?php
                    }
                        echo $message['text'];
                    ?>
                    </div>
                    <?php
                    }
                    ?>
                </div>
            </div>
        </div>
    </div>
    <script>$('#flash-messages').modal('show');</script>
    <?php 
      }
    ?>


    <footer class="footer">
      <div class="container">
        <span class="text-muted">ilBonus S.P.A.- admin: calogero.monachello@unipa.it</span>
      </div>
    </footer>

  </body>
</html>

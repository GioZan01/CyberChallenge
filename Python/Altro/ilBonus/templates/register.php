
<div class='text-center mt-5'>
    <form class="form-signin" method="post" action="/register">
        <h1 class="h3 mb-3 font-weight-normal">Registrati</h1>
        <label for="inputUser" class="sr-only">Username</label>
        <input name="email" type="email" id="inputUser" class="form-control group" placeholder="Email" required autofocus>
        <label for="inputPassword" class="sr-only">Password</label>
        <input name="password" type="password" id="inputPassword" class="form-control group" placeholder="Password" required>
        <label for="inputPassword2" class="sr-only">Password (confirmation)</label>
        <input name="password_confirm" type="password" id="inputPassword2" class="form-control" placeholder="Password (verifica)" required>
        <button class="btn btn-lg btn-primary btn-block" type="submit">Registrati!</button>
        <p>o <a href="/login">Accedi</a></p>
    </form>
</div>
</div>

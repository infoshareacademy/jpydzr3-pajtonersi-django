user_create_get = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</head>
<body>
<!-- Nav Bar -->
<nav class="navbar navbar-dark bg-primary">
    <div class="container-xxl">
        <span class="fw-bold text-light">
            Placówka Medyczna
        </span>
    </div>
</nav>

<!-- Block content for other templates to reuse -->
<div class="container">
    
<form method="post">
    <input type="hidden" name="csrfmiddlewaretoken" value="H36js0S4M1btfU8l8ulCVhWZU37xqMNeO8xLPZRiEDL49eVrEo24NXPuCvuUq3AT">
    <p><label for="id_password">Password:</label> <input type="text" name="password" maxlength="128" required id="id_password"></p>
<p><label for="id_last_login">Last login:</label> <input type="text" name="last_login" id="id_last_login"></p>
<p><label for="id_is_superuser">Superuser status:</label> <input type="checkbox" name="is_superuser" id="id_is_superuser"> <span class="helptext">Designates that this user has all permissions without explicitly assigning them.</span></p>
<p><label for="id_groups">Groups:</label> <select name="groups" id="id_groups" multiple>
</select> <span class="helptext">The groups this user belongs to. A user will get all permissions granted to each of their groups.</span></p>
<p><label for="id_user_permissions">User permissions:</label> <select name="user_permissions" id="id_user_permissions" multiple>
  <option value="1">admin | log entry | Can add log entry</option>

  <option value="2">admin | log entry | Can change log entry</option>

  <option value="3">admin | log entry | Can delete log entry</option>

  <option value="4">admin | log entry | Can view log entry</option>

  <option value="9">auth | group | Can add group</option>

  <option value="10">auth | group | Can change group</option>

  <option value="11">auth | group | Can delete group</option>

  <option value="12">auth | group | Can view group</option>

  <option value="5">auth | permission | Can add permission</option>

  <option value="6">auth | permission | Can change permission</option>

  <option value="7">auth | permission | Can delete permission</option>

  <option value="8">auth | permission | Can view permission</option>

  <option value="13">auth | user | Can add user</option>

  <option value="14">auth | user | Can change user</option>

  <option value="15">auth | user | Can delete user</option>

  <option value="16">auth | user | Can view user</option>

  <option value="17">contenttypes | content type | Can add content type</option>

  <option value="18">contenttypes | content type | Can change content type</option>

  <option value="19">contenttypes | content type | Can delete content type</option>

  <option value="20">contenttypes | content type | Can view content type</option>

  <option value="21">sessions | session | Can add session</option>

  <option value="22">sessions | session | Can change session</option>

  <option value="23">sessions | session | Can delete session</option>

  <option value="24">sessions | session | Can view session</option>

  <option value="37">users | address | Can add address</option>

  <option value="38">users | address | Can change address</option>

  <option value="39">users | address | Can delete address</option>

  <option value="40">users | address | Can view address</option>

  <option value="25">users | user | Can add user</option>

  <option value="26">users | user | Can change user</option>

  <option value="27">users | user | Can delete user</option>

  <option value="28">users | user | Can view user</option>

  <option value="29">users | user | Can add user</option>

  <option value="30">users | user | Can change user</option>

  <option value="31">users | user | Can delete user</option>

  <option value="32">users | user | Can view user</option>

  <option value="33">users | recepcjonista | Can add recepcjonista</option>

  <option value="34">users | recepcjonista | Can change recepcjonista</option>

  <option value="35">users | recepcjonista | Can delete recepcjonista</option>

  <option value="36">users | recepcjonista | Can view recepcjonista</option>

</select> <span class="helptext">Specific permissions for this user.</span></p>
<p><label for="id_username">Username:</label> <input type="text" name="username" maxlength="150" required id="id_username"> <span class="helptext">Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</span></p>
<p><label for="id_first_name">First name:</label> <input type="text" name="first_name" maxlength="150" id="id_first_name"></p>
<p><label for="id_last_name">Last name:</label> <input type="text" name="last_name" maxlength="150" id="id_last_name"></p>
<p><label for="id_email">Email address:</label> <input type="email" name="email" maxlength="254" id="id_email"></p>
<p><label for="id_is_staff">Staff status:</label> <input type="checkbox" name="is_staff" id="id_is_staff"> <span class="helptext">Designates whether the user can log into this admin site.</span></p>
<p><label for="id_is_active">Active:</label> <input type="checkbox" name="is_active" id="id_is_active" checked> <span class="helptext">Designates whether this user should be treated as active. Unselect this instead of deleting accounts.</span></p>
<p><label for="id_date_joined">Date joined:</label> <input type="text" name="date_joined" value="2021-12-12 11:14:08" required id="id_date_joined"><input type="hidden" name="initial-date_joined" value="2021-12-12 11:14:08" id="initial-id_date_joined"></p>
<p><label for="id_pesel">Pesel:</label> <input type="text" name="pesel" maxlength="20" id="id_pesel"></p>
<p><label for="id_tel_no">Tel no:</label> <input type="text" name="tel_no" maxlength="20" id="id_tel_no"></p>
<p><label for="id_address">Address:</label> <select name="address" id="id_address">
  <option value="" selected>---------</option>

</select></p>
    <input type="submit" value="Zatwierdź">
</form>

</div>
</body>
</html>"""
const email = document.forms["login_form"]["email"];
const password = document.forms["login_form"]["password"];

//Password validation
password.addEventListener("input", function (event) {
  let password_reg = /^[A-Za-z\d]+$/;

  if(!password_reg.test(password.value)) {
    password.setCustomValidity("Используются только латинские буквы и цифры!");
  } else {
    password.setCustomValidity("");
  }
});

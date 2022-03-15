$(document).ready(function () {
  $(".single-date-field").mask("00/00/0000", {
    placeholder: "_ _ /_ _ /_ _ _ _",
  });
});

//login
function login() {
  //validation check

  //set session
  sessionStorage.setItem("username", "User1");
}
//logout
function logout() {
  // window.localStorage.clear();
  sessionStorage.clear();
}

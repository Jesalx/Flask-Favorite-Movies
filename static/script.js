/* eslint-disable no-unused-vars */
function meetsLoginConditions() {
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;
  const errMsg = document.getElementById('messages');

  if (username.length === 0 || password.length === 0) {
    errMsg.innerText = 'Please fill in all fields.';
    return false;
  }

  return true;
}

function meetsSignupConditions() {
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;
  const repassword = document.getElementById('repassword').value;
  const errMsg = document.getElementById('messages');

  if (username.length === 0 || password.length === 0 || repassword.length === 0) {
    errMsg.innerText = 'Please fill in all fields.';
    return false;
  }

  // How to use regular expressions in Javascript from:
  // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions
  const usernameRe = /^[0-9a-zA-Z]+$/;
  if (!username.match(usernameRe)) {
    errMsg.innerText = 'Username may only contain alphanumeric characters.';
    return false;
  }

  const passwordRe = /^[0-9a-zA-Z!@#$]+$/;
  if (!password.match(passwordRe)) {
    errMsg.innerText = 'Password may only contain alphanumeric characters and !, @, #, $';
    return false;
  }

  if (username.length > 32) {
    errMsg.innerText = 'Username must be 32 or less characters.';
    return false;
  }

  if (password.length <= 4) {
    errMsg.innerText = 'Password must be 5 or more characters.';
    return false;
  }

  if (password.length > 128) {
    errMsg.innerText = 'Password must be 128 or less characters.';
    return false;
  }

  if (password !== repassword) {
    errMsg.innerText = 'Passwords must match.';
    return false;
  }

  if (username === password) {
    errMsg.innerText = 'Username and password must not match.';
    return false;
  }

  return true;
}

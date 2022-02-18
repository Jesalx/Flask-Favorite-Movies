function meetsLoginConditions() {
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;
    let err_msg = document.getElementById("messages");

    if (username.length === 0 || password.length === 0) {
        err_msg.innerText = "Please fill in all fields."
        return false;
    }

    return true;
}
function LogIn(){
    var defaultUsername = "admin"
    var defaultPassword = "123456"

    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    if (username === defaultUsername && password === defaultPassword){
        window.location.href = "/lc_ql"
    } else {
        alert("Tên đăng nhập hoặc mật khẩu không đúng!");
    }
}
document.getElementById("login").addEventListener("click", LogIn)
document.addEventListener("keydown", function(event) {
    if (event.code === "Enter") {
      LogIn()
    }
})

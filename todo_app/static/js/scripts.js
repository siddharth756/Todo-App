const paths = window.location.pathname;
const navs = document.querySelectorAll(".sign_login");
let nav_item = document.getElementsByClassName("sign_login")[0];

navs.forEach((e)=>{
    const path_url = new URL(e.href).pathname;

    if (paths === path_url ) {
        nav_item.innerHTML="SIGNUP";
        nav_item.href = '/login/';
    }
    else {
        nav_item.innerHTML="LOGIN";
    }
})
var burger = document.querySelector("nav .hamburger");
var menu = document.querySelector("nav .navbar ul");
var menu_background1 = document.querySelector(".menu_background1");
var menu_background2 = document.querySelector(".menu_background2"); 
var logo = document.querySelector(".navigation .logo"); 

burger.addEventListener("click", () => {
    burger.classList.toggle("active");
    menu.classList.toggle("active");
    menu_background1.classList.toggle("active");
    menu_background2.classList.toggle("active"); 
    logo.classList.toggle("active"); 
})
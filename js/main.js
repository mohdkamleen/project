let main_div = document.getElementById("main_div");  
let preloader = document.querySelector("div.preloader");  
let preloader_counter = document.querySelector("div.preloader span b"); 
let nav_hamberger_background = document.querySelector(".nav_hamburger_background");  
let nav_background = document.querySelector(".nav_background"); 
let scroll_down = document.querySelector(" .scroll_down");  
let scroll_top = document.querySelector(" .scroll_top");  
let style = document.getElementById("style"); 
let mousemove = document.getElementById("mousemove");
let down = document.getElementsByClassName("scroll_down")[0];

window.onload = () => {
    preloader.classList.add("active"); 
    nav_background.classList.add("show"); 
}  
 

window.onscroll = () => {
    let windowPageYOffset = window.pageYOffset; 

    if(windowPageYOffset > 400){
        nav_hamberger_background.classList.add("show");  
    } else {
        nav_hamberger_background.classList.remove("show");
    }  
    
    // scroll behaviour css html   
    nav_background.style.top = -0.3 * windowPageYOffset + "px";
    down.style.top = -0.5 * windowPageYOffset + "px";
    main_div.style.top = -0.5 * windowPageYOffset + "px";
}
 

/// ////////splash screen counter /////////////
var count_number = 0; 
let preloader_counter_function = setInterval(function(){
    count_number++;
    preloader_counter.innerHTML = count_number; 
    
    if (count_number == 100){
        clearInterval(preloader_counter_function);
    }
},13) 


//////////////////// window change color and background////////////
window.onclick = () => {
    let arr = [
        "", "", "css/change/blue.css",
        "", "", "css/change/blue2.css",
        "", "", "css/change/blue3.css",
        "", "", "css/change/red.css",
        "", "", "css/change/red2.css",
        "", "", "css/change/red3.css",
        "", "", "css/change/green.css",
        "", "", "css/change/green2.css",
        "", "", "css/change/yellow.css",
        "", "", "css/change/yellow2.css",
        "", "", "css/change/gray.css",
        "", "", "css/change/gray2.css",
        "", "", "css/change/pink.css",
        "", "", "css/change/cyan.css",
        "", "", "css/change/cyan2.css",
        "", "", "css/change/red.css"
    ]
  
   let styleSheet = arr[Math.floor(Math.random() * arr.length)];
   style.setAttribute("href", styleSheet);
}



///////////////// mousemove code  ///////////////
window.onmousemove  = () => {
            var a = document.createElement("p");
            a.setAttribute("id", "mousemove");
            document.body.appendChild(a);
            a.style.left = event.clientX + 'px';
            a.style.top = event.clientY + 'px';
            var col = ["yellow","green","blue","red","pink","cyan","black"];
            var mcol = col[Math.floor(Math.random()*col.length)];
            a.style.transition = "all 1s linear";
            a.style.left = a.offsetLeft - 20 + "px";
           a.style.top = a.offsetTop - 20 + "px";
           a.style.height = "50px";
           a.style.width = "50px";
           a.style.borderWidth = "2px"; 
           a.style.opacity = 0;
           a.style.borderColor = mcol;
          }

  

 
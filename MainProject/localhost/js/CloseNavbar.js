let closenahuy = document.querySelectorAll("[at-attr='close_btn']")[0];
closenahuy.onclick = function() {
    document.querySelectorAll("[class='m-sidebar-visible m-prevent-scrolling']")[0].className = "";
}
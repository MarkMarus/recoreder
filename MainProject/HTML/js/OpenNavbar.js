let elem = document.querySelectorAll("[class='l-header__menu__item m-avatar-item m-avatar-item']")[0];
elem.onclick = function() {
    document.querySelectorAll("[class='']")[0].className = "m-sidebar-visible m-prevent-scrolling";
}
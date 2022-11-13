let elem = document.querySelectorAll("[class='l-header__menu__item m-avatar-item m-avatar-item']")[0];
elem.onclick = function() {
    document.querySelectorAll("[class='p-list-chats']")[0].className = "p-list-chats m-sidebar-visible m-prevent-scrolling";
}
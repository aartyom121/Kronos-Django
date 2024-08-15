const navButton = document.getElementById('navButton');
const navMenu = document.getElementById('navMenu');
const forAdminLink = document.getElementById('for_admin');
let timeout;

forAdminLink.addEventListener('mouseover', function() {
    clearTimeout(timeout);
    navMenu.style.display = 'block';
});

forAdminLink.addEventListener('mouseout', function() {
    timeout = setTimeout(function() {
        navMenu.style.display = 'none';
    }, 500); // задержка в 500 миллисекунд перед скрытием меню
});

navMenu.addEventListener('mouseover', function() {
    clearTimeout(timeout);
});

navMenu.addEventListener('mouseout', function() {
    timeout = setTimeout(function() {
        navMenu.style.display = 'none';
    }, 500); // задержка в 500 миллисекунд перед скрытием меню
});

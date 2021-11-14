document.addEventListener('DOMContentLoaded', function() {
    var collapse = document.querySelectorAll('.collapsible');
    M.Collapsible.init(collapse, {
        accordion: false
    });
});

var elem = document.querySelector('.sidenav');
var instance = new M.Sidenav(elem);
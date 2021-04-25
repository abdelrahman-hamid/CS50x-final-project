// Dynamically assigns the active class to the currently clicked page

$(document).ready(function() {
    // Get current path and find target link
    var path = window.location.pathname;
    var target = $('#collapsibleNavbar a[href="'+path+'"]');

    // Add active class to target link
    target.addClass('active');
});
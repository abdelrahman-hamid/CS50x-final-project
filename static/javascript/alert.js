// Displays the success alert when the contact form is submitted successfully

$(document).ready(function() {
    $('#feedback').hide();
    $('form').submit(function() {
        $('#feedback').show();
    });
});
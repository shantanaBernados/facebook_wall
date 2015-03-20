$(document).ready(function() {
    $('#status_form').on('submit', function(e) {
        e.preventDefault();
        var temp = $('#id_post').val();
        console.log(temp);
        alert(temp);
    });
});

$(document).ready(function() {
    $('#status_form').on('submit', function(e) {
        // e.preventDefault();
        // var temp = $('#id_post').val();
        // // console.log(temp);
        // // alert(temp);
        // $('#posts').prepend('<p>' + temp + '</p>');
        $.ajax(
            url: "/post",
            type: "POST",
            data: { the_post : $('#id_post').val() },

            success: function(data) {
                alert('asdasd')
            }
            
        );
    });
});

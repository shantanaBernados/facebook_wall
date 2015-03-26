$(document).ready(function() {
    $('#status_form').on('submit', function(e) {
        e.preventDefault();
        $.ajax({
            url: 'post',
            type: "post",
            data: { 
                post : $('#id_post').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() 
            },

            success: function(data) {
                console.log(data);
                $('#posts').prepend(data);
                $('#id_post').val('');
                console.log('success');
            },

            error: function(error) {
                console.log('FAIL');
            }
            
        });
    });
});

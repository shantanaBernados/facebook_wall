$(document).ready(function() {
    $('#status_form').on('submit', function(e) {
        e.preventDefault();
        $.ajax({
            url: 'post',
            type: "post",
            data: { 
                post: $('#id_post').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() 
            },

            success: function(data) {
                $('#posts').prepend(data);
                $('#id_post').val('');
                console.log('success');
            },

            error: function(error) {
                console.log('FAIL');
            }
            
        });
    });

    $('.like_post').click(function(e) {
        e.preventDefault();
        var post_id = $(this).attr('id');
        console.log(post_id);
        $.ajax({
            url: 'like',
            type: 'get',
            data: {
                'post_id': post_id,
            },

            success: function(data) {
                $(this)
                console.log('SUCCESS');
            },

            error: function(error) {
                console.log('ERROR');
            }
        });
    });
});

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
                var first_post = $('#posts-container .posts:first');
                if (first_post.length > 0) {
                    $(data).hide().insertBefore(first_post).fadeIn('slow');
                } else {
                    $(data).hide().appendTo($('#posts-container')).fadeIn('slow');
                }
                $('#posts-container textarea').elastic();
                $('#id_post').val('');
                $('#id_post').focus();
                console.log('success!');
            },

            error: function(error) {
                console.log('FAILED TO POST');
            }

        });
    });

    $(document).on("click", '.like', function(e){
        e.preventDefault();
        elem = $(this);
        $.ajax({
            url: 'like',
            type: 'get',
            data: {
                post_id : $(this).attr('id')
            },

            success: function(data) {
                console.log(data);
                if (data.html != '') {
                    elem.next().remove();
                    $(data.html).hide().insertAfter(elem).fadeIn('slow');
                } else {
                    $(elem).next().fadeOut('slow', function() {
                        $(this).remove();
                    });
                }
                elem.text(data.label);
                console.log('SUCCESS');
            },

            error: function(error) {
                console.log('FAILED TO LIKE POST');
            }
        });
    });

    $(document).on('click', '.delete_post', function(e) {
        e.preventDefault();
        elem = $(this);
        $.ajax({
            url: 'delete_post',
            type: 'get',
            data: {
                post_id: elem.attr('id')
            },

            success: function(data) {
                $('#' + elem.attr('id')).fadeOut('slow', function() {
                    $(this).remove();
                });
                console.log('SUCCESS');
            },

            error: function(error) {
                console.log('FAILED TO DELETE POST');
            }
        });
    });

    $('#posts-container textarea').elastic();
});

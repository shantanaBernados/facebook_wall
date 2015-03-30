$(document).ready(function() {
    $('#status_form').on('submit', function(e) {
        e.preventDefault();
        $.post('post', $(this).serialize(), function(data) {
            var first_post = $('#posts-container .posts:first');
            if (first_post.length > 0) {
                $(data).hide().insertBefore(first_post).fadeIn('slow');
            } else {
                $(data).hide().appendTo($('#posts-container')).fadeIn('slow');
            }
            $('#posts-container textarea').elastic();
            $('#id_post').val('');
            $('#id_post').focus();
        });
    });

    $(document).on("click", '.like', function(e){
        e.preventDefault();
        elem = $(this);
        $.get('like', {post_id: elem.attr('id')}, function(data) {
            if (data.html != '') {
                elem.next().remove();
                $(data.html).hide().insertAfter(elem).fadeIn('slow');
            } else {
                $(elem).next().fadeOut('slow', function() {
                    $(this).remove();
                });
            }
            elem.text(data.label);
        });
    });

    $(document).on('click', '.delete_post', function(e) {
        e.preventDefault();
        elem = $(this);
        $.get('delete_post', {post_id: elem.attr('id')}, function(data) {
             $('#' + elem.attr('id')).fadeOut('slow', function() {
                $(this).remove();
            });
        });
    });

    $(document).on('click', '.edit_post', function(e) {
        e.preventDefault();
        elem = $(this);
        console.log(elem.parent());
    });

    $('#posts-container textarea').elastic();
});

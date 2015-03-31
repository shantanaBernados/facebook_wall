$(document).ready(function() {

    var setCSRFToken = function(xhr) {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            if (cookies[i].indexOf('csrftoken') == 0) {
                xhr.setRequestHeader('X-CSRFToken', cookies[i].split('=')[1]);
                break;
            }
        }
    }

    $.ajaxSetup({
       beforeSend: setCSRFToken
    });

    $('#posts-container textarea').elastic();

    $(document).on('focus', '#posts-container textarea', function() {
        $(this).elastic();
    });

    $('#status_form').on('submit', function(e) {
        e.preventDefault();
        if ($('#id_post').val().trim() == "") {
            alert('STATUS/POST is blank!');
        } else {
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
        }
    });

    $(document).on("click", '.like', function(e){
        e.preventDefault();
        elem = $(this);
        $.post('like', {post_id: elem.attr('id')}, function(data) {
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

    $(document).on('click', '.del_post', function(e) {
        e.preventDefault();
        elem = $(this);
        $.post('delete_post', {post_id: elem.attr('id')}, function(data) {
            $('#' + elem.attr('id')).fadeOut('slow', function() {
                $(this).remove();
            });
        });
    });

    $(document).on('click', '.edit_post', function(e) {
        e.preventDefault();
        elem = $(this);
        var textarea = elem.parent().find('textarea');
        textarea.removeAttr('disabled').focus();
        elem.next().show();
        elem.hide();
    });

    $(document).on('click', '.save_post', function(e){
        e.preventDefault();
        elem = $(this);
        var textarea = elem.parent().find('textarea');
        if (textarea.val().trim() == "") {
            alert('STATUS/POST is blank!');
        } else {
            var data = {
                post_id: $(this).attr('id'),
                new_post: textarea.val()
            };
            $.post('save_post', data, function() {
                textarea.prop('disabled', true);
                elem.hide().prev().show();
                elem.parent().find('.edit-tag').show();
            });    
        }
    }); 
});

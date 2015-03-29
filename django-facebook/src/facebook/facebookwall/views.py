import json

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.views import generic
from forms import PostForm, RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic.edit import FormView, CreateView
from django.template.loader import render_to_string

from django.contrib.auth.models import User
from models import Post, Like


# Create your views here.


@login_required(login_url='/login/')
def index(request):
    posts = Post.objects.all()
    for post in posts:
        # likes = Like.objects.filter(post=post)
        post.likers = User.objects.filter(like__post=post)
        if request.user in post.likers:
            post.like_label = 'Unlike'
        else:
            post.like_label = 'Like'   
    return render(request, 'facebookwall/index.html',
                  {'form': PostForm(), 'posts': posts})


class SignupView(CreateView):
    template_name = 'facebookwall/signup.html'
    form_class = RegisterForm
    fields = ['username', 'email', 'password']
    success_url = '/login/'


def post(request):
    if request.is_ajax:
        if request.method == 'POST':
            p = Post.objects.create(
                user=request.user,
                post=request.POST.get('post')
            )
            p.save()
            html = render_to_string('facebookwall/post.html', {'post': p})
            return HttpResponse(html)


def like(request):
    if request.is_ajax:
        post_id = request.GET.get('post_id')
        post = Post.objects.get(id=post_id)
        label = ''
        try:
            like = Like.objects.create(
                user=request.user,
                post=Post.objects.get(id=post_id)
            )
            like.save()
            label = 'Unlike'
        except:
            Like.objects.get(post=post, user=request.user).delete()
            label = 'Like'

        response = {'html': ''}
        response['label'] = label
        post.likers = User.objects.filter(like__post=post)
        if post.likers:
            html = render_to_string(
                'facebookwall/likes.html',
                {'post': post, 'user': request.user}
            )
            response['html'] = html
        return HttpResponse(json.dumps(response), content_type="application/json")

    return HttpResponseRedirect('/')


def delete_post(request):
    if request.is_ajax:
        Post.objects.get(id=request.GET.get('post_id')).delete()
        return HttpResponse('Success')

    return HttpResponseRedirect('/')
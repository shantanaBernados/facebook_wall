from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic.edit import FormView, CreateView
from django.template.loader import render_to_string

from forms import PostForm, RegisterForm, LoginForm
from models import Post, Like

# Create your views here.


@login_required(login_url='/login/')
def index(request):
    print PostForm()
    posts = Post.objects.all()
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

    return HttpResponseBadRequest()


def like(request):
    print request
    if request.is_ajax:
        p_id = request.GET.get('post_id')
        post = Post.objects.get(id=p_id)
        try:
            like = Like.objects.create(
                user=request.user,
                post=post
            )
            like.save()
            return HttpResponse()
        except:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return HttpResponse()

    return HttpResponseBadRequest()

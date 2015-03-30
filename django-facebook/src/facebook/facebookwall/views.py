import json

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.views.generic.edit import FormView, CreateView
from django.template.loader import render_to_string

from forms import PostForm, RegisterForm, LoginForm
from django.contrib.auth.models import User
from models import Post, Like


# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'facebookwall/index.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        posts = Post.objects.all()
        for post in posts:
            post.likers = User.objects.filter(like__post=post)
            if self.user in post.likers:
                post.like_label = 'Unlike'
            else:
                post.like_label = 'Like'
        context = {
            'form': PostForm(),
            'posts': posts
        }
        return context


class SignupView(CreateView):
    template_name = 'facebookwall/signup.html'
    form_class = RegisterForm
    fields = ['username', 'email', 'password']
    success_url = '/login'


class PostView(generic.View):
    def post(self, request):
        p = Post.objects.create(
            user=request.user,
            post=request.POST.get('post')
        )
        p.save()
        html = render_to_string('facebookwall/post.html', {'post': p})
        return HttpResponse(html)


class LikeView(generic.View):
    def post(self, request):
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)
        label = ''
        try:
            like = Like.objects.create(
                user=request.user,
                post=post
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
        return HttpResponse(json.dumps(response),
                            content_type="application/json")


class DeletePostView(generic.View):
    def post(self, request):
        Post.objects.get(id=request.POST.get('post_id')).delete()
        return HttpResponse('Success')

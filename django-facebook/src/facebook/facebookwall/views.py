from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from forms import PostForm, RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic.edit import FormView, CreateView
from django.template.loader import render_to_string

from models import Post

# Create your views here.


@login_required(login_url='/login/')
def index(request):
    posts = Post.objects.all()
    print posts
    return render(request, 'facebookwall/index.html',
                  {'form': PostForm(), 'posts': posts})


class SignupView(CreateView):
    template_name = 'facebookwall/signup.html'
    form_class = RegisterForm
    fields = ['username', 'email', 'password']
    success_url = '/login/'


def log_sign(request):
    return render(request, 'facebookwall/login.html',
                  {'form_log': LoginForm(), 'form_reg': RegisterForm()})


# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         if user.is_active:
#             login(request, user)


# def signup(request):
#     print request
#     username = request.POST.get('username')
#     password = request.POST['password1']
#     password2 = request.POST['password2']
#     email = request.POST.get('email')
#     # try:
#     #     User.objects.get(username='test4')
#     # except:
#     #     if password == password2:
#     #         u = User.objects.create_user(username, email, password)
#     u = User.objects.create_user(username, email, password)
#     u.save()
#     login(request, user)
#     return HttpResponseRedirect('/')


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


def comment(request):
    pass


def get_posts(request):
    pass


def get_comments(request):
    pass

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/')
def index(request):
    return render(request, 'facebookwall/index.html', {'form': PostForm()})


def post(request):
    pass


def comment(request):
    pass


def get_posts(request):
    pass


def get_comments(request):
    pass

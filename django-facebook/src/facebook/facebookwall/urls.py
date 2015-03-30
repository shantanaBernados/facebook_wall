from django.conf.urls import patterns, include, url
from facebookwall import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post$', views.PostView.as_view(), name='post'),
    url(r'^like$', views.LikeView.as_view(), name='like'),
    url(r'^delete_post$', views.DeletePostView.as_view(), name='delete_post'),
    url(r'^save_post$', views.SavePostView.as_view(), name='save_post'),
)

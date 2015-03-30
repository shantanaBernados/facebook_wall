from django.conf.urls import patterns, include, url
from facebookwall import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'facebook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post$', views.PostView.as_view(), name='post'),
    url(r'^like$', views.LikeView.as_view(), name='like'),
    url(r'^delete_post$', views.DeletePostView.as_view(), name='delete_post')
    #url(r'^comment/$', views.comment, name='comment')

)

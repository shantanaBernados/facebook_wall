from django.conf.urls import patterns, include, url
from facebookwall import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'facebook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^post$', views.post, name='post'),
    #url(r'^comment/$', views.comment, name='comment')
    
)

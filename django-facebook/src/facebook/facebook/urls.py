from django.conf.urls import patterns, include, url
from django.views.generic.edit import CreateView
from facebookwall import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'facebookwall/login.html'}, name='login'),
    # url(r'^login/$', views.log_sign, name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout',
        {'next_page': 'login'}, name='logout'),
    url(r'^', include('facebookwall.urls', namespace='wall')),
    url(r'^signup/', views.SignupView.as_view(), name='signup')
)

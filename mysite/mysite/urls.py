"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, url, include
from django.contrib import admin
from mysite.views import hello, current_datetime, hours_ahead
from books import views

urlpatterns = [
    url(r'^$', views.home),
    url('^hello/$', hello),
    url(r'^admin/', include(admin.site.urls)),
    url('^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^search/$', views.search),
    url(r'^ISBN/(?P<isbn>[0-9]+)/$', views.show),
    url(r'^delete/(?P<isbn>[0-9]+)/$', views.delete),
    url(r'^home/$', views.home),
]


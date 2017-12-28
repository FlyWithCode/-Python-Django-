"""env5 URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django_web import views
from article import views as article_views
from article.views import RSSFeed

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', article_views.home),
    url(r'^$', views.index),
    url(r'^detail(?P<id>\d+)/$',article_views.detail,name="content"),
    url(r'^tag(?P<tag>\w+)/$',article_views.searchtag,name="search_tag"),
    url(r'^search/$',article_views.blog_search,name='search'),
    url(r'^feed/$',RSSFeed(),name='RSS'),

]

"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from appBlog import views
from appBlog.views import PostsListView, PostDetailView, ProjectListView, VideoListView, TutorialListView

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^$', PostsListView.as_view(), name='list'),
    url(r'^articles_project$', ProjectListView.as_view(), name='project'),      #
    url(r'^articles_video$', VideoListView.as_view(), name='video'),          #
    url(r'^$', TutorialListView.as_view(), name='tutorial'),    #
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()),
    url(r'^$', views.create, name='create'),
    url(r'^(?P<pk>\d+)/$', views.show),
]

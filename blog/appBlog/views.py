from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from appBlog.models import Articles, Comments
from django.views.generic import ListView, DetailView

class PostsListView(ListView):
    model = Articles

class ProjectListView(ListView):
    model = Articles

    def get_queryset(self):
        return Articles.objects.filter(tag='project')[:5]

class VideoListView(ListView):
    model = Articles

    def get_queryset(self):
        return Articles.objects.filter(tag='video')[:5]

class TutorialListView(ListView):
    model = Articles

    def get_queryset(self):
        return Articles.objects.filter(tag='tutorial')[:5]

class PostDetailView(DetailView):
    model = Articles

def show(request):
    comments = Comments.objects.all()
    return render(request, "articles_detail.html", {"comments": comments})

def create(request):
    if request.method == "POST":
        com = Comments()
        com.name = request.POST.get("name")
        com.text = request.POST.get("text")
        com.save()
    return HttpResponseRedirect('Articles.id')#return HttpResponseRedirect('/')





# Create your views here.

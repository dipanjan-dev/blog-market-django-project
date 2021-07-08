from django.shortcuts import render
from home.models import upload_blog
from django.contrib import messages
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage

# Create your views here.


def index(request):
     blog = upload_blog.objects.all()
     blogs = {'blogs': blog}
     return render(request, 'index.html',blogs)


def about(request):
     return render(request, 'about.html')

def contact(request):
     return render(request, 'contact.html')

def support(request):
     return render(request, 'support.html')

def post(request , blog_title):
     post = upload_blog.objects.filter(blog_title=blog_title).first()
     allblog = upload_blog.objects.all()
     blogs = {'blogs': post , 'blogposts': allblog}
     return render(request, 'post.html',blogs)


def search(request):
     post = request.GET['post']
     blog = upload_blog.objects.filter(blog_title__icontains = post)
     blogs = {'blogs': blog ,'posts' : post}
     return render(request, 'search.html',blogs)
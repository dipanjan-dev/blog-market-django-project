from django.urls import path
from django.urls import URLPattern
from . import views
from home.models import upload_blog

urlpatterns = [
    path('', views.index , name='index'),
    path('search' , views.search,name='search'),
    path('about' , views.about,name='about'),
    path('contact-us' , views.contact,name='contact'),
    path('support-us' , views.support,name='support'),
    path('post/<str:blog_title>/', views.post, name='post')
]


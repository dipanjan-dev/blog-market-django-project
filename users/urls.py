from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.syslogout,name='syslogout'),
    path('profile',views.profile,name='profile'),    
]

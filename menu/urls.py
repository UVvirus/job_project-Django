from django.urls import path
from . import views
urlpatterns=[
    path('',views.menu,name='menu'),
    path('home',views.home,name='home'),
    path('login',views.login,name='login'),
    path('resume',views.resume,name='resume'),
    path('vacancy',views.vacancy,name='vacancy'),
    path('signup',views.signup,name='signup'),


]
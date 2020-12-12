from django.urls import path
from django.views.generic.base import RedirectView
from . import views
urlpatterns=[
    path('signup',views.signup,name='signup'),
    path('login',views.Login,name='login'),
]
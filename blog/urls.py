# from django import urls

from . import views
from django.urls import path
urlpatterns=[
    path('home/',views.home ,name='home'),
    path('post/',views.post,name='post'),
    path('about-us/',views.aboutus,name='about-us'),
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),

]


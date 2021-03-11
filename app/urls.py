from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('recipe', views.recipe, name='recipe'),
    path('contact', views.contact, name='contact'),
    path('contact', views.contact, name='contact'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),



]

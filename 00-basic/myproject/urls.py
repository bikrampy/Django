from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', views.apiHome, name='apiHome'),
    path('about/', views.about, name='about'),
    path('api/about/', views.apiAbout, name='apiAbout'),
    path('profile/', views.profile),
    path('portfolio/', views.portfolio),
    path("blogs/", include("blog.urls")),
]

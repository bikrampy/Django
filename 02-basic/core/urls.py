from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('dummyform/', views.dummyform, name='dummyform'),
    path('studentform/', views.studentform, name='studentform'),
]

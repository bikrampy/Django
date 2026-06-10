from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dummyform/', views.dummyform, name='dummyform'),
    path('studentform/', views.studentform, name='studentform'),
    path("signup/", views.signup, name='signup'),
    path("login/", views.login_user, name='login'),
    path("logout/", views.logout_user, name='logout'),
    path("dashboard/", views.dashboard, name='dashboard'),
]

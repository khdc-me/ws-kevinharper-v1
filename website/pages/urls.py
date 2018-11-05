from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('experience/', views.experience, name='experience'),
    path('my-portal/', views.my_portal, name='my-portal'),
    path('my-projects/', views.my_projects, name='my-projects'),
]

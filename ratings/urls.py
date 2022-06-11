from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='api'),
    path('', views.apiOverView, name='api'),
    path('project/', views.showprojects, name='project-list'),
    path('project/<int:pk>', views.showproject, name='project'),
    path('projectcreate/', views.createproject, name='create'),
    path('profile/', views.showprofiles, name='project-list'),
    path('profile/<int:pk>', views.showprofile, name='project'),


]
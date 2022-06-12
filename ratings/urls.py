from django.urls import path
from . import views

urlpatterns = [
    path('apis', views.apiOverView, name='api'),
    path('projects/', views.showprojects, name='project-list'),
    path('project/<int:pk>', views.showproject, name='project'),
    path('projectcreate/', views.createproject, name='create'),
    path('projectupdate/<int:pk>', views.showproject, name='update'),
    path('delete/<int:pk>', views.showproject, name='delete'),
    path('profiles/', views.showprofiles, name='project-list'),
    path('profile/<int:pk>', views.showprofile, name='project'),


]
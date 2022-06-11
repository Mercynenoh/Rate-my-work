from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='api'),
    path('', views.apiOverView, name='api'),
    path('project/', views.showprojects, name='project-list'),
    path('profile/', views.showprofiles, name='project-list'),

]
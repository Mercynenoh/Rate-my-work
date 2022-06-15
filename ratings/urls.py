from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_results, name='search_results'),
    path('apis', views.apiOverView, name='api'),
    path('projects/', views.showprojects, name='project-list'),
    path('image/<str:pk>', views.viewProject, name='image'),
    path('projects/<int:pk>', views.showproject, name='project'),
    path('review/', views.submitreview, name='review'),
    # path('projectcreate/', views.createproject, name='create'),
    # path('projectupdate/<int:pk>', views.showproject, name='update'),
    # path('delete/<int:pk>', views.showproject, name='delete'),
    path('profiles/', views.showprofiles, name='project-list'),
    path('profiles/<int:pk>', views.showprofile, name='project'),


]
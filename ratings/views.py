from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def apiOverView(request):
    api_urls ={
        'List':"/project-list/",
        'Detail View':"/project-detail/<int:id>",
        'Create':"/project-create",
        'Update':"/project-update/<int:id>",
        'Delete':"/project-delete/<int:id>",

    }

    return Response('api_urls');
@apiOverView(['GET'])
def showall(request):
    projects = Project.objects.all()
    profiles = Profile.objects.all()
      

    

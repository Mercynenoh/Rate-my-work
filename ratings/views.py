from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Project, Profile
from .serializers import ProjectSerializer, ProfileSerializer

# Create your views here.
def home(request):
    return render ( request, 'project/home.html')
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
@api_view(['GET'])
def showprojects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def showproject(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createproject(request):
    serializer = ProjectSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def showprofiles(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def showprofile(request, pk):
    profile = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(profile, many=True)
    return Response(serializer.data)


      

    

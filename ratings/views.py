from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Project, Profile
from .serializers import ProjectSerializer, ProfileSerializer
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ReviewForm
from django.contrib import messages

# Create your views here.
class ProjectList(ListView):
    model = Project
    template_name = 'project/project_list.html'

    def get_queryset(self):
        return Project.objects.all()

def project_list(request):
    projects = models.Project.objects.all()
    return render(request, "project/project_list.html", {'project':project})

class ProfileList( ListView):
    model = Profile
    template_name = 'project/profile_list.html'

    def get_queryset(self):
        return Profile.objects.all()

def profile_list(request):
        profiles = models.Profile.objects.all()
        return render(request, "project/post_list.html", {'profiles':profiles})


def viewProject(request, pk):
    project = Project.objects.get(id=pk)
    return render(request, 'project/project.html', {'project':project})


class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['image', 'title', 'description', 'link', 'author']
    success_url = '/'

class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    fields = ['pic', 'bio', 'email', 'phone', 'author', 'project']
    success_url = '/profile/'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('/login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def submitreview(request):
    if request.method == 'POST':
        form =ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Your review has been submitted')
            return redirect('/')
           
        else:
            form =ReviewForm(request.POST)
            if form.is_valid():
                data=Reviewrating()
                data.rating = form.cleaned_data.get('rating')
                data.save()
                messages.success(request, 'Your review has been submitted')
            return redirect('/')

def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_author(search_term)
        message = f"{search_term}"

        return render(request, 'project/search.html',{"message":message,"projects": searched_projects})

    else:
        message = "Ooops we can't find that!!"
        return render(request, 'project/search.html',{"message":message})
  
        
@api_view(['GET'])
def apiOverView(request):
    api_urls ={
        'List':"/project-list/",
        'Detail View':"/project-detail/<int:id>",
        'Create':"/project-create",
        'Update':"/projectupdate/<int:id>",
        'Delete':"/projectdelete/<int:id>",

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

@api_view(['POST'])
def updateproject(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(instance=project, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def deleteproject(request, pk):
    project = Project.objects.get(id=pk)
    project.delete()
    return Response('Project deleted successfully')


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

@api_view(['POST'])
def createprofile(request):
    serializer = ProfileSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateprofile(request, pk):
    project = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(instance=profile, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


      

    

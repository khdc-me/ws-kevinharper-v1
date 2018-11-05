from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def experience(request):
    return render(request, 'experience.html', {})


def my_portal(request):
    return render(request, 'my-portal.html', {})


def my_projects(request):
    return render(request, 'my-projects.html', {})

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def experience(request):
    return render(request, 'experience.html', {})
from django.http import HttpResponse
from django.shortcuts import render
import os

from .models import News, Activities, Projects

# Create your views here.
def index(request):
    return render(request, 'index/index.html')

def about(request):
    return render(request, 'index/about.html')

def news(request):
    news = News.objects.order_by('-created_date')
    context = {'news': news}
    return render(request, 'index/news.html', context)

def albom(request):
    return render(request, 'index/albom.html')

def photo(request, photo_folder):
    directory = os.getcwd() + '/nadezhda51/index/static/images/photo/' + photo_folder
    files = os.listdir(directory)
    images = list(filter(lambda x: x.endswith('.jpg'), files))
    for key, value in enumerate(images):
        images[key] = 'http://localhost/static/images/photo/' + photo_folder + '/' + value
    context = {'images': images}
    return render(request, 'index/photo.html', context)

def activities(request):
    activities = Activities.objects.order_by('-created_date')
    context = {'activities': activities}
    return render(request, 'index/activities.html', context)

def projects(request):
    projects = Projects.objects.order_by('-created_date')
    context = {'projects': projects}
    return render(request, 'index/projects.html', context)

def details(request):
    return render(request, 'index/details.html')

def people(request):
    return render(request, 'index/people.html')

def reviews(request):
    return render(request, 'index/reviews.html')

def thanks(request):
    return render(request, 'index/thanks.html')

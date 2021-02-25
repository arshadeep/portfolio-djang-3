from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
#here we will grab our project obejcts from the databse and send them forward into the templates

def home(request):
    projects=Project.objects.all()#this grab everything from the databse and turns them into python objects
    return render(request,'portfolio/home.html',{'projects':projects})

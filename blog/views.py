from django.shortcuts import render,get_object_or_404
from .models import Blogs

def all_blogs(request):
    blog=Blogs.objects.all()#this is a list hence you can apply all the functions that can be put on list
    #blog=Blogs.object.order_by('date') this wont give all the objects but this will give us the recent object added
    return render(request,'blog/all_blogs.html',{"blogs":blog})

def detail(request,blog_id):
    blog=get_object_or_404(Blogs,pk=blog_id)
    return render(request,'blog/detail.html',{'blog':blog})


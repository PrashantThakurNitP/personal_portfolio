from django.shortcuts import render,get_object_or_404
#get_object_or_404 is used to import one particular object
# Create your views here.
from django.http import HttpResponse
from .models import project_blog

def all_blogs(request):
	projects_blog=project_blog.objects.order_by("-date") #it shows only top 5 current blog on first page
	#grab all object of project class from data base and put in variable projects 
	#return render(request,'portfolia/home.html')
	return render(request,'blog/all_blogs.html',{'projects_blog':projects_blog})
"""
# Create your views here.
def home(request):
	projects=project.objects.all() #grab all object of project class from data base and put in variable projects 
	return render(request,'portfolia/home.html',{'projects':projects})
	#through dictionary we can pass all project objects with projects variable and we can acess from wepage
	#if we acess it to webpage it will show queryset whch similar to list
	"""
def detail(request,blog_id): #blog_id is integer that is present after /blog/
	blog=get_object_or_404(project_blog,pk=blog_id) #project_blog is name of class and pk is primary key
	#in pk we assign blog_id
	return render(request,'blog/detail.html',{'blog':blog})
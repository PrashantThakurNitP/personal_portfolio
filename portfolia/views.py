from django.shortcuts import render
from django.http import HttpResponse
import random

from .models import project

# Create your views here.
def home(request):
	projects=project.objects.all() #grab all object of project class from data base and put in variable projects 
	return render(request,'portfolia/home.html',{'projects':projects})
	#through dictionary we can pass all project objects with projects variable and we can acess from wepage
	#if we acess it to webpage it will show queryset whch similar to list
from django.contrib import admin

# Register your models here.
from .models import project #here only .model is mentioned as it is present inside same floder as in admin.py

admin.site.register(project) #this line say we want to see project model innside admin



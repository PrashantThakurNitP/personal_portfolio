from django.db import models


# Create your models here.
class project_blog(models.Model): # this class inherit from model class
		title=models.CharField(max_length=200) #in paranthesis we can specify words in title
		description=models.TextField(max_length=1000)
		date=models.DateField()
		def __str__(self):
			return self.title
		#see model fiels documention
		#image=models.ImageField(upload_to='portfolia/images' )
		""" , height_field=None, width_field=None, max_length=100 """
		#in upload to you chose name of folder you want to upload to
		#url=models.URLField(max_length=200, blank=True) #we can add blank=true in all above field if donot want
		 #to take it empty

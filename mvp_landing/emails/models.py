from django.db import models




# Create your models here.
class EmailEntry(models.Model):
    email = models.EmailField()
    name =models.CharField(max_length=120, blank=True)
    bio = models.TextField(max_length=120, blank=True)
   
   #add
    updated = models.DateTimeField(auto_now=True)# set when saved?

   #time
    timestamp = models.DateTimeField(auto_now_add=True) # set when add?
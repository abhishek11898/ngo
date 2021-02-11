from django.db import models
from django.utils import timezone

# Create your models here.

class News(models.Model):
    photo= models.ImageField(upload_to="myimage")
    time=models.DateTimeField(auto_now_add=True)
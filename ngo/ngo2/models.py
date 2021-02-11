from django.db import models
import string

# Create your models here.
 
class Newsmodel(models.Model):
    newsid=models.AutoField(primary_key=True)
    newsphoto= models.ImageField(upload_to="myimage")
    newscreatetime=models.DateTimeField(auto_now_add=True)
    newstitle=models.CharField(max_length=200)
    newspost=models.TextField()
    class Meta:
        db_table="News"

class Tributemodel(models.Model):
    tributeid=models.AutoField(primary_key=True)
    tributephoto= models.ImageField(upload_to="myimage")
    tributecreatetime=models.DateTimeField(auto_now_add=True)
    tributetitle=models.CharField(max_length=200)
    tributepost=models.TextField()
    class Meta:
        db_table="Tribute"

class Quotesmodel(models.Model):
    quotesid=models.AutoField(primary_key=True)
    quotesphoto= models.ImageField(upload_to="myimage")
    quotescreatetime=models.DateTimeField(auto_now_add=True)
    quotestitle=models.CharField(max_length=200)
    class Meta:
        db_table="Quotes"
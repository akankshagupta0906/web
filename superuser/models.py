from django.db import models
from django.contrib.auth.models import User
from WebDaity.models import UserProfile

# Create your models here.
class Service(models.Model):
    service = models.CharField(max_length=100)
    img = models.ImageField(upload_to="service",blank=True)

class Plans(models.Model):
    plan_name = models.CharField(max_length=100) 
    price_mon = models.IntegerField(default=00)
    price_year = models.IntegerField(default=00)
    month = models.IntegerField(default=00)
    year = models.IntegerField()

class DelPlan(models.Model):
    plan_n= models.ForeignKey(Plans,on_delete=models.CASCADE)
    plan = models.CharField(max_length=300)
    
class Project(models.Model):
    proimg = models.ImageField(upload_to="hotel_images",blank=True)
    no = models.CharField(max_length=50)
    pro_name = models.CharField(max_length=100,default="webdeity")
    prolink = models.CharField(max_length=700)

class Blog(models.Model): 
    titel = models.CharField(max_length=200)
    blog = models.CharField(max_length=10000,default="blog")
    



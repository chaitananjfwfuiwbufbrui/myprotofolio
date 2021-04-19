from django.db import models

    

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from personal.utils import unique_slug_generator
import requests
# class domain(models.Model):
#     domainname = models.CharField(max_length=20)
    
#     def __str__(self):
#         return self.domainname
# Create your models here.
class projects(models.Model):
    project_name = models.CharField(max_length=50)
    projects_image = models.ImageField()
    
    project_gitlink = models.CharField(max_length=2000)
    project_demo = models.CharField(max_length=2000)
    domainname = models.CharField(max_length=20)
    # projects = models.ForeignKey(domain,on_delete=models.SET_NULL,blank=True,null=True)
    def __str__(self):
        return self.project_name 

class blog(models.Model):
    user  = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    title = models.CharField(max_length=15)
    photo = models.ImageField(upload_to = 'users/%y/%m/%d',blank = True)
    pub_date = models.DateField()
    body = models.TextField()
    slug = models.SlugField(blank=True,null=True)
def slug_generator(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(slug_generator,sender=blog)
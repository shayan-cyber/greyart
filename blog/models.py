from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=50)
    social_media_link = models.CharField(max_length=250)
    timeStamp = models.DateTimeField(blank=True)
    image = models.ImageField(upload_to = 'shop/images',default="")
    slug = models.CharField(max_length=150)
    views = models.IntegerField(default=0)


    def __str__(self):
        return self.title + ' by ' + self.author
class poem(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    
    author = models.CharField(max_length=50)
    social_media_link = models.CharField(max_length=250)
    timeStamp = models.DateTimeField(blank=True)
    image = models.ImageField(upload_to = 'shop/images',default="")
    slug = models.CharField(max_length=150)
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.title + ' by ' + self.author
class meme(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    
    author = models.CharField(max_length=50)
    social_media_link = models.CharField(max_length=250)
    timeStamp = models.DateTimeField(blank=True)
    image = models.ImageField(upload_to = 'shop/images',default="")
    slug = models.CharField(max_length=150)
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.title + ' by ' + self.author







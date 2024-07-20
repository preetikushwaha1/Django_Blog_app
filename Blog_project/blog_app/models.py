from django.db import models
from django.contrib.auth.models import User 
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(datetime.now())
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="Comments", on_delete = models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField(max_length=300)
    created_date = models.DateField()
    
    def __str__(self):
        return self.text
    
    
    
    
    
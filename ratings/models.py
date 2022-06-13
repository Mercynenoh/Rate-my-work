from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    image = models.ImageField(upload_to = 'articles/',default='IMAGE')
    title =  models.CharField(max_length =30)
    description = models.TextField()
    link = models.CharField(max_length =100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title

class Profile(models.Model):
    pic = models.ImageField(upload_to = 'articles/',default='IMAGE')
    bio =  models.CharField(max_length =100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    email = models.CharField(max_length =30)
    phone =  models.CharField(max_length =10)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.bio

class Reviewrating(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject =  models.CharField(max_length =50, blank=True)
    review = models.TextField(blank=True)
    rating = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.subject
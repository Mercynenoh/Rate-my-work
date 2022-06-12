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
    image = models.ImageField(upload_to = 'articles/',default='IMAGE')
    bio =  models.CharField(max_length =100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    email = models.CharField(max_length =30)
    phone =  models.CharField(max_length =10)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.bio
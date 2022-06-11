from django.db import models

# Create your models here.
class Project(models.Model):
    image = models.ImageField(upload_to = 'articles/',default='IMAGE')
    title =  models.CharField(max_length =30)
    description = models.TextField()
    link = models.CharField(max_length =30)
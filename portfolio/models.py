from django.db import models

# Create your models here.
class projects(models.Model):
    name= models.CharField(max_length=255)
    image= models.CharField(max_length=2500)
    des=models.TextField()


class form(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    message=models.TextField()

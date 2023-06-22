from django.db import models


# Create your models here.
class Books(models.Model):
    objects = ['title', 'author', 'price', 'email']
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    email = models.EmailField(default="")

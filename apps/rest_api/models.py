from django.db import models


# Create your models here.
class Books(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    email = models.EmailField(blank=True)


class Album(models.Model):
    artist = models.ForeignKey(Books, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    # Way to write many to many relational field
    # art = models.ManyToManyField(Books)


class Runner(models.Model):
    MedalType = models.TextChoices("MedalType", "GOLD SILVER BRONZE")
    name = models.CharField(max_length=60)
    medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)

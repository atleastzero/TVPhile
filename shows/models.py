from django.db import models

class Show(models.Model):
    name = models.CharField(max_length=200)
    likes = models.IntegerField()
    last_liked = models.DateTimeField()

class Tag(models.Model):
    name = models.ManyToManyField(Show)
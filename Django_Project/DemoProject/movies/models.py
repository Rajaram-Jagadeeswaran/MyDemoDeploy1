from django.db import models
from django import forms

class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=30)
    release_date = models.PositiveIntegerField()  # Corrected field name
    genre = models.CharField(max_length=200)
    duration = models.FloatField()

    def __str__(self):
        return self.title
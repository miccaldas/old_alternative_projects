from django.db import models
from django.urls import reverse
from django import forms


class Bookmarks(models.Model):
    title = models.CharField(max_length=100)
    comment = models.TextField()
    link = models.URLField(max_length=200)
    k1 = models.CharField(max_length=100)
    k2 = models.CharField(max_length=100)
    k3 = models.CharField(max_length=100)
    tempo = models.DateTimeField()

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("new")

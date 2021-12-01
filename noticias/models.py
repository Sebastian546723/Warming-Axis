from django.db import models


class News(models.Model):
    Title = models.CharField(max_length=100, blank=True)
    Description = models.CharField(max_length=100, blank=True)
    ImgNews = models.CharField(max_length=100, blank=True)
    URL = models.CharField(max_length=98, blank=True)
    Source = models.CharField(max_length=100, blank=True)

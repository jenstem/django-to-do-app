from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=100)
    priority = models.IntegerField()
    # add app to settings.py

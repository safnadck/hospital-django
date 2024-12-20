from django.db import models

class Departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()

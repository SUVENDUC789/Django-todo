from django.db import models

# Create your models here.

class Todo(models.Model):
    name=models.CharField(max_length=130)
    title=models.CharField(max_length=1150)
    note=models.CharField(max_length=99130)

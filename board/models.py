from django.db import models

# Create your models here.
class board(models.Model):
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    name = models.CharField(max_length=10)
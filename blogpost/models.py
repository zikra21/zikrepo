from django.db import models

# Create your models here.
class Blogpost(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    summary = models.TextField()
    image = models.ImageField(upload_to='images/')
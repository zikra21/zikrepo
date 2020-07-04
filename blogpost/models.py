from django.db import models


class Blogpost(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    summary = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def body(self):
        return self.summary[:100]

    def pub_date(self):
        return self.date.strftime('%b %e %Y')
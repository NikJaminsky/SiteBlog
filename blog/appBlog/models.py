from django.db import models
from ckeditor.fields import RichTextField

class Articles(models.Model):
    title = models.CharField(max_length=50)
    preview = models.TextField(max_length=250)
    content = RichTextField()
    date = models.DateField()
    tag = models.CharField(max_length=10)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "%i/" % self.id

class Comments(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    text = models.TextField(max_length=150)

class Message(models.Model):
    name = models.CharField(max_length=20)
    text = models.TextField(max_length=350)

# Create your models here.

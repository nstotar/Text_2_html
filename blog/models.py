from django.db import models

from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Post(models.Model):
    body = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.body
# myapp/models.py
from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)

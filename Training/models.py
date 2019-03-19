from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now())

class SA():
    pass

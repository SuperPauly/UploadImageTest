from django.db import models

# Create your models here.


class Post(models.Model):
    tile = models.CharField(max_length=64)


class Images(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField()
    k = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

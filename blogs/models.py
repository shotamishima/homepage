from django.db import models


class Blogs(models.Model):
    image = models.ImageField(upload_to='images/')
    text = models.CharField(max_length=200)

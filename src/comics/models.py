from django.db import models


class Comics(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    rating = models.FloatField(default=0)



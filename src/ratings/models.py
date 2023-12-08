from django.db import models

from comics.models import Comics
from users.models import User


class Rating(models.Model):
    comics = models.ForeignKey(Comics, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    value = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.username

from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class User(AbstractUser):
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(
        max_length=11,
        unique=True,
    )
    username = models.CharField(max_length=45, unique=True)
    is_developer = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()
    USERNAME_FIELD = "phone_number"

    def __str__(self):
        return self.phone_number


class OtpCode(models.Model):
    phone_number = models.CharField(max_length=11, unique=True)
    code = models.CharField(max_length=6)

    def __str__(self) -> str:
        return f"{self.phone_number} --- {self.code}"


# Every user can add an app to hes/her wishlist
class BookMark(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, default=None)
    app = models.ForeignKey("applications.App", on_delete=models.PROTECT)

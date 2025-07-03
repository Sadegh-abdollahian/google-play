from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from applications.models import App


class User(AbstractUser):
    phone_number = models.CharField(
        max_length=11,
        unique=True,
        verbose_name="شماره موبایل",
    )
    username = models.CharField(max_length=45, verbose_name="نام کاربری")

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
class wishListItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, default=None)
    app = models.ForeignKey(App, on_delete=models.PROTECT)

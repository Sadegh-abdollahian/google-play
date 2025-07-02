from django.db import models
from .validators import validate_image_size, validate_max_age, validate_max_rate
from taggit.managers import TaggableManager
from core.settings import AUTH_USER_MODEL


class Category(models.Model):
    name = models.CharField(max_length=30)
    position = models.PositiveIntegerField()
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name


class App(models.Model):
    STATUS_CHOICES = (
        ("draft", "در انتظار انتشار"),
        ("published", "منتشر شده"),
        ("deleted", "حذف شده"),
    )
    apk_file = models.FileField()
    name = models.CharField(max_length=100)
    subname = models.CharField(max_length=150)
    icon_image = models.ImageField(validators=[validate_image_size])
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="draft",
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="apps"
    )
    legal_age = models.PositiveSmallIntegerField(validators=[validate_max_age])
    downloads = models.PositiveIntegerField()
    about = models.CharField(max_length=4000)
    price = models.PositiveIntegerField()
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)
    tags = TaggableManager()

    def __str__(self):
        return self.name


# This model is for the images of the app that are shown in the previews section.
class AppImage(models.Model):
    position = models.PositiveSmallIntegerField(unique=False)
    image_file = models.ImageField()
    app = models.ForeignKey(App, on_delete=models.PROTECT)

    def __str__(self):
        return self.app.name


class Review(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT)
    app = models.ForeignKey(App, on_delete=models.PROTECT)
    text = models.CharField(max_length=3000)
    rating = models.PositiveSmallIntegerField(validators=[validate_max_rate])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

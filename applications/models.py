from django.db import models
from .validators import validate_icon_image_size, validate_max_age, validate_max_rate
from taggit.managers import TaggableManager
from core.settings import AUTH_USER_MODEL
from django.utils import timezone
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=30)
    position = models.PositiveIntegerField()
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

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
    icon_image = models.ImageField(
        upload_to="app-icons/",
        validators=[validate_icon_image_size],
    )
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
    owner = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True, blank=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("updated",)

    def get_app_owner(self):
        return self.owner.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Resize icon image to 800x800
        if self.icon_image:
            img = Image.open(self.icon_image.path)
            output_size = (800, 800)
            img = img.resize(output_size)
            img.save(self.icon_image.path)


def get_upload_to(instance):
    return "upload/%d/" % (instance.app.name)


# This model is for the images of the app that are shown in the previews section.
class AppImage(models.Model):
    position = models.PositiveSmallIntegerField(unique=False)
    image_file = models.ImageField(upload_to=get_upload_to)
    app = models.ForeignKey(App, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.app.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Resize icon image to 1920x1080
        if self.image_file:
            img = Image.open(self.image_file.path)
            output_size = (1920, 1080)
            img = img.resize(output_size)
            img.save(self.image_file.path)


class Review(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT)
    app = models.ForeignKey(App, on_delete=models.PROTECT)
    text = models.CharField(max_length=3000)
    rating = models.PositiveSmallIntegerField(validators=[validate_max_rate], default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ("updated",)

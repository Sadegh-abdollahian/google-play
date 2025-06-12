from django.contrib import admin
from .models import App, Category, AppImage, Review

# Register your models here.
admin.site.register(App)
admin.site.register(Category)
admin.site.register(AppImage)
admin.site.register(Review)

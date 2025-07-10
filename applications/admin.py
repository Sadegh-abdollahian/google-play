from django.contrib import admin
from .models import App, Category, AppImage, Review


# Register your models here.
@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "subname",
        "status",
        "category",
        "downloads",
        "price",
        "slug",
        "owner",
        "created",
    ]
    list_filter = ["status", "category"]
    search_fields = ["name", "owner"]
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ["updated", "created"]


@admin.register
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "position",
        "slug",
    ]
    list_filter = ["name"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ["updated", "created"]


@admin.register
class ReviewAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "app",
        "text",
        "rating",
        "created",
        "updated",
    ]
    list_filter = ["text", "rating"]
    search_fields = ["text", "app", "name"]
    readonly_fields = ["updated", "created"]


admin.site.register(AppImage)

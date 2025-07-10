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


admin.site.register(Category)
admin.site.register(AppImage)
admin.site.register(Review)

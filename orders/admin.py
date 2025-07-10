from django.contrib import admin
from .models import Order


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "app",
        "total_amount",
        "status",
        "created",
        "updated",
    ]
    list_filter = ["status", "total_amount"]
    search_fields = ["user", "app"]
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ["updated", "created"]

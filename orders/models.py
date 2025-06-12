from django.db import models
from core.settings import AUTH_USER_MODEL
from applications.models import App


# Create your models here.
class Order(models.Model):
    STATUS_CHOICES = (
        ("draft", "در انتظار پرداخت"),
        ("purchased", "پرداخت شده"),
        ("deleted", "حذف شده"),
    )
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT)
    app = models.ForeignKey(App, on_delete=models.PROTECT)
    total_amount = models.PositiveIntegerField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="draft")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.app.name} --- {self.user.phone_number} --- {self.total_amount}"

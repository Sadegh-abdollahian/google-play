from django.contrib import admin
from .models import User, OtpCode, wishListItem

# Register your models here.


admin.site.register(User)
admin.site.register(OtpCode)
admin.site.register(wishListItem)

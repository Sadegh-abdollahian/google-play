from rest_framework import serializers
from applications.models import App, Category
from orders.models import Order


class AppSerializer(serializers.ModelSerializer):

    class Meta:
        model = App
        fields = "__all__"
        lookup_field = "slug"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get("request")

        user = request.user if request else None

        if instance.price == 0 or (user.is_authenticated and user.is_superuser):
            return representation

        if (
            user.is_authenticated
            and Order.objects.filter(
                user=user, app=instance, status="purchased"
            ).exists()
        ):
            return representation

        representation.pop("apk_file", None)
        return representation


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"

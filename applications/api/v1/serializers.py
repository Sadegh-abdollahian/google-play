from rest_framework import serializers
from applications.models import App, Category
from orders.models import Order


class AppSerializer(serializers.ModelSerializer):

    class Meta:
        model = App
        fields = "__all__"
        lookup_field = "slug"

    def to_representation(self, instance):
        """
        This function deletes the apk_file field for the users that haven't purchased the app yet
        """
        representation = super().to_representation(instance)
        request = self.context.get("request")

        user = request.user if request else None

        # Checks if the app is free or the user is superuser and returns it with full details
        if instance.price == 0 or (user.is_authenticated and user.is_superuser):
            return representation

        # Checks if the user has purchased the app and returns it with full details
        if (
            user.is_authenticated
            and Order.objects.filter(
                user=user, app=instance, status="purchased"
            ).exists()
        ):
            return representation

        # Checks if the user is the developer of the app and returns it with full details
        if instance.owner == user:
            return representation

        # Finally if the users hasn't purchased that app, this line cuts the apk_file off and returns the rest of the app details
        representation.pop("apk_file", None)
        return representation


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"
        lookup_field = "slug"

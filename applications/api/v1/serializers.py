from rest_framework import serializers
from applications.models import App, Category


class AppSerializer(serializers.ModelSerializer):

    class Meta:
        model = App
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"

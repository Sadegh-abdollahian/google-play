import django_filters
from applications.models import App


class AppFilter(django_filters.FilterSet):
    class Meta:
        model = App
        fields = {
            "name": ["exact", "contains"],
            "price": ["exact", "lt", "gt", "range"],
            "category": ["exact"],
        }

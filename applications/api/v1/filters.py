import django_filters
from applications.models import App


class AppFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    min_legal_age = django_filters.NumberFilter(
        field_name="legal_age", lookup_expr="gte"
    )
    max_legal_age = django_filters.NumberFilter(
        field_name="legal_age", lookup_expr="lte"
    )
    min_downloads = django_filters.NumberFilter(
        field_name="downloads", lookup_expr="gte"
    )
    max_downloads = django_filters.NumberFilter(
        field_name="downloads", lookup_expr="lte"
    )
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = App
        fields = [
            "name",
            "min_price",
            "max_price",
            "min_legal_age",
            "max_legal_age",
            "min_downloads",
            "max_downloads",
        ]

# *****************************************************************************
# supporters/filters.py
# *****************************************************************************

import django_filters

from .models import Supporter

# *****************************************************************************
# SupporterFilter
# *****************************************************************************


class SupporterFilter(django_filters.FilterSet):

    first_name = django_filters.CharFilter(
        field_name='first_name',
        lookup_expr='exact',
    )
    last_name = django_filters.CharFilter(
        field_name='last_name',
        lookup_expr='exact',
    )
    email = django_filters.CharFilter(
        field_name='email',
        lookup_expr='exact',
    )
    district_tag = django_filters.CharFilter(
        field_name='address__district__tag',
        lookup_expr='exact',
    )
    district_name = django_filters.CharFilter(
        field_name='address__district__name',
        lookup_expr='exact',
    )
    cause_tag = django_filters.CharFilter(
        field_name='causes__tag',
        lookup_expr='exact',
    )
    cause_name = django_filters.CharFilter(
        field_name='causes__name',
        lookup_expr='exact',
    )

    class Meta:
        model = Supporter
        fields = (
            'first_name',
            'last_name',
            'email',
            'district_tag',
            'district_name',
            'cause_tag',
            'cause_name',
        )

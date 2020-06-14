# *****************************************************************************
# supporters/views.py
# *****************************************************************************

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets, mixins, permissions
from rest_framework.response import Response

from .models import District, Supporter
from .serializers import DistrictSerializer, SupporterSerializer

# *****************************************************************************
# DistrictViewSet
# *****************************************************************************

class DistrictViewSet(mixins.CreateModelMixin, 
                      mixins.ListModelMixin, 
                      mixins.UpdateModelMixin, 
                      mixins.RetrieveModelMixin, 
                      viewsets.GenericViewSet):
    
    """
    A ViewSet to CREATE, LIST, UPDATE, and RETRIEVE districts

    """

    filter_backend = (
        filters.OrderingFilter,
        filters.SearchFilter
    )
    ordering = ['-updated_on']
    ordering_fields = ['created_on', 'updated_on']
    permission_classes = [permissions.IsAuthenticated]
    queryset = District.objects.all()
    search_fields = ['name', 'tag']
    serializer_class = DistrictSerializer


# *****************************************************************************
# SupporterViewSet
# *****************************************************************************

class SupporterViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):

    """
    A ViewSet to CREATE, LIST, UPDATE, and RETRIEVE districts

    """

    filter_backend = (
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    )
    ordering = ['-updated_on']
    ordering_fields = ['created_on', 'updated_on']
    permission_classes = [permissions.IsAuthenticated]
    queryset = Supporter.objects.all()
    search_fields = [
        'first_name', 'last_name', 'email', 'address__district__tag',
        'address__district__name', 'causes__tags', 'causes__name'
    ]
    serializer_class = SupporterSerializer

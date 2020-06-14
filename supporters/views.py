# *****************************************************************************
# supporters/views.py
# *****************************************************************************

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets, mixins, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .filters import SupporterFilter
from .models import Cause, District, Supporter
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

    filter_backends = (
        DjangoFilterBackend,
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

    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    )
    filter_class = SupporterFilter
    ordering = ['-updated_on']
    ordering_fields = ['created_on', 'updated_on']
    permission_classes = [permissions.IsAuthenticated]
    queryset = Supporter.objects.all()
    search_fields = [
        'first_name', 'last_name', 'email', 'address__district__tag',
        'address__district__name', 'causes__tags', 'causes__name'
    ]
    serializer_class = SupporterSerializer

    @action(detail=False)
    def stats(self, request):
        """
        Returns the counts of supporters who follow a given cause

        """

        queryset = self.get_queryset()
        cause_names = Cause.objects.values_list('name', flat=True)

        stats = {}
        for cause_name in cause_names:
            num_supporters = Supporter.objects.filter(
                causes__name=cause_name
            ).count()
            
            if stats.get(cause_name):
                stats[cause_name] += num_supporters
            else:
                stats[cause_name] = num_supporters
            
        return Response(stats, status.HTTP_200_OK)

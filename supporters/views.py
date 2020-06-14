from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
# *****************************************************************************
# supporters/views.py
# *****************************************************************************

from rest_framework import viewsets, mixins, permissions
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

    permission_classes = [permissions.IsAuthenticated]
    queryset = District.objects.all()
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
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SupporterSerializer
    queryset = Supporter.objects.all()
    #allow searching of supporter by cause

    def get_queryset(self):
        print('tokenTest', self)
        cause = self.request.query_params.get('cause', None)
        if cause is not None:
            queryset = queryset.filter(causes__tag=cause)

        zip = self.request.query_params.get('zip', None)
        if zip is not None:
            queryset = queryset.filter(address__zipcode=zip)

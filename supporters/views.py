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

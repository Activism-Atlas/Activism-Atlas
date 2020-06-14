# *****************************************************************************
# supporters/urls.py
# *****************************************************************************

from django.conf.urls import include, url
from rest_framework.routers import SimpleRouter

from . import views

# *****************************************************************************
# Routers
# *****************************************************************************

router = SimpleRouter()

router.register(r'districts', views.DistrictViewSet)

# *****************************************************************************
# urlconfs
# *****************************************************************************

app_name = 'supporters'

urlpatterns = [
    url(r'^', include(router.urls))
]

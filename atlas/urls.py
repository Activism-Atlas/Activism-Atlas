# *****************************************************************************
# atlas/urls.py
# *****************************************************************************

from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token

# *****************************************************************************
# urlpatterns
# *****************************************************************************

urlpatterns = [
    url(r'api/', include('api.urls')),
    url(r'admin/', admin.site.urls),
    url(r'auth/token', obtain_jwt_token),
]

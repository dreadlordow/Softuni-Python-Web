from django.contrib import admin
from django.urls import path, include
import common


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('common.urls')),
    path('pets/', include('pets.urls'))
]

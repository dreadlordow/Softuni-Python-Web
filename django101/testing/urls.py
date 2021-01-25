from django.urls import path

from testing.views.index import index

urlpatterns = [
    path('', index, name='profiles'),
]
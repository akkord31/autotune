from django.urls import path
from .views import access_table_view

urlpatterns = [
    path('', access_table_view, name='access_table'),
]

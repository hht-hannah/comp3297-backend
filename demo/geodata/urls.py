"""
Urls for geodata app.
"""

from django.urls import path
from geodata.views import GeoDataRecordView, GeoDataSearchView

app_name = 'geodata'
urlpatterns = [
    path('create/', GeoDataRecordView.as_view(), name='create'),
    path('search/', GeoDataSearchView.as_view(), name='search')]
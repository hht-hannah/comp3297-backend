"""
Urls for core app.
"""

from django.urls import path
from core.views import UserLoginView

app_name = 'core'
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),]
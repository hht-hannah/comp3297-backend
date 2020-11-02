"""
Services for core module.
"""

from django.contrib.auth import authenticate, get_user_model, \
    models as auth_models
from rest_framework.authtoken.models import Token
from .serializers import UserInfoSerializer
from .models import UserInfo



def create_authentication_token(data):
    """User Authentication

    Parameters
    ----------
    data: json format
        Data containing username and password

    Returns
    -------
    token: Token
        if the authentication passed.
    None if the authentication failed.
    """
    user = authenticate(
        username=data.get("username", ""),
        password=data.get("password", ""))
    if user is not None:
        return Token.objects.get_or_create(user=user)
    return None

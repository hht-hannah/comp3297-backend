from django.shortcuts import render

# Create your views here.
# -*- coding: UTF-8 -*-

"""
Register and Login.
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserInfoSerializer
from .services import (create_authentication_token)



class UserLoginView(APIView):
    """
    A class based view for User Login.
    """

    def post(self, request):
        """User Authentication

        Parameters
        ----------
        request: json format
            Data containing request information, or None.

        Returns
        -------
        response: json format
            return "Login Failed" if authentication failed.
            return the token if the authentication passed.
        """
        token = create_authentication_token(request.data)
        if token is None:
            return Response(
                "Login Failed",
                status=status.HTTP_401_UNAUTHORIZED
            )
        return Response(
            {"token": token.key},
            status=status.HTTP_200_OK
        )
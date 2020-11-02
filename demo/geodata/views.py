import json
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import GeoDataSerializer
from .services import create_geodata, search_geodata

class GeoDataRecordView(APIView):
    """
    A class based view for creating and fetching GeoData Record.
    """ 

    def post(self, request):
        """
        Creates a GeoData record
        """
        add_data = create_geodata(request.data)
        return Response(
            GeoDataSerializer(add_data).data,
            status=status.HTTP_201_CREATED
        )

class GeoDataSearchView(APIView):
    """
    A class based view for fetching GeoData Record from the given api.
    """

    def post(self, request):
        """
        Search a GeoData record
        """
        result = search_geodata(request.data)
        to_return = []
        if result != None: 
            for r in json.loads(result):
                to_return.append(GeoDataSerializer(r).data)
            return Response(
                to_return,
                status=status.HTTP_200_OK
            )
        return Response("No such location or error during search.", stauts=status.HTTP_404_NOT_FOUND)
    

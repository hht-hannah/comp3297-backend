from rest_framework import serializers
from .models import GeoData

class GeoDataSerializer(serializers.ModelSerializer):
    """
    Serializer that serializes/deserializes UserInfo object
    """

    class Meta:
        """
        Meta Information
        """
        model = GeoData
        fields = (
            'addressZH',
            'nameZH',
            'x',
            'y',
            'nameEN',
            'addressEN',
        )

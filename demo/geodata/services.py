import requests, json
from .models import GeoData

def create_geodata(position_data):
    """
    Creates a GeoData record
    """
    geodata = GeoData.objects.create(
        addressZH=position_data.get("addressZH"),
        nameZH=position_data.get("nameZH"),
        x=position_data.get("x"),
        y=position_data.get("y"),
        addressEN=position_data.get("addressEN"),
        nameEN=position_data.get("nameEN"),
    )
    
    return geodata

def search_geodata(search_data): 
    """
    Creates a GeoData record
    """
    url = 'https://geodata.gov.hk/gs/api/v1.0.0/locationSearch?'
    params = {"q": search_data.get("search")}
    response = requests.get(url=url, params=params)
    if response.status_code == 200:
        return response.content
    return None
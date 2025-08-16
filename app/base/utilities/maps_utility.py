import os
import requests
import time
import logging
from dotenv import load_dotenv
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderQuotaExceeded

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_address_suggestions(query, country_code='dk', limit=100):
    """
    Fetch detailed address suggestions using GeoPy with Nominatim.
    
    Args:
        query (str): Partial address to autocomplete (e.g., 'Stenmaglevej 6, 2700 Brønshøj')
        country_code (str, optional): ISO country code to filter results (default: 'dk' for Denmark)
        limit (int): Number of suggestions to return
    
    Returns:
        list: List of address suggestions with coordinates and detailed components
    """
    # Initialize Nominatim geocoder with a user agent
    geolocator = Nominatim(user_agent="bolig-recommendation")
    
    try:
        # Respect Nominatim's rate limit (1 request/second)
        time.sleep(1.0)
        
        # Perform geocoding with addressdetails and country filter
        locations = geolocator.geocode(
            query,
            exactly_one=False,
            limit=limit,
            addressdetails=True,
            country_codes=[country_code],
            language='da'  # Set language to Danish for better results
        )
        
        results = []
        if locations:
            for location in locations:
                address = location.raw.get('address', {})
                formatted_address = location.raw.get('display_name', '')
                
                address_info = {
                    'address': formatted_address,
                    'latitude': location.latitude,
                    'longitude': location.longitude,
                    'street': address.get('road', ''),
                    'house_number': address.get('house_number', ''),
                    'postcode': address.get('postcode', ''),
                    'city': address.get('city', '') or address.get('town', '') or address.get('village', ''),
                    'country': address.get('country', '')
                }
                results.append(address_info)
        
        return results
    
    except (GeocoderTimedOut, GeocoderQuotaExceeded) as e:
        logger.warning(f"Geocoding timeout or quota exceeded for query '{query}': {e}")
        return []
    except Exception as e:
        logger.error(f"Error during geocoding for query '{query}': {e}")
        return []

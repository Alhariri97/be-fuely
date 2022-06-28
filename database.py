from dotenv import load_dotenv
load_dotenv()
import os
apiKey = os.getenv("googleAPIKey")

import googlemaps
gmaps = googlemaps.Client(key = apiKey)

def get_petrol_stations(lat, lon):
    result = gmaps.places( location=(f"{lat}, {lon}"), radius=2, type="gas_station")
    return result["results"]

from typing import Dict
from dotenv import load_dotenv
load_dotenv()
import os
apiKey = os.getenv("googleAPIKey")

import googlemaps
gmaps = googlemaps.Client(key = apiKey)

def get_petrol_stations(lat, lon):
    result = gmaps.places( location=(f"{lat}, {lon}"), radius=2, type="gas_station")
    #loop through list/array, return wanted values
    #place_id, name, formatted_address, geometry.location.lat // lng, 

    arr = list
    obj = dict

    #for station in result["results"]:
        #obj["name"] = station["name"]
        #print(station["name"])
    print(obj)
    return result["results"]



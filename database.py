import googlemaps
gmaps = googlemaps.Client(key = "")



def get_petrol_stations(lat, lon):
    result = gmaps.places( location=(f"{lat}, {lon}"), radius=2, type="gas_station")
    return result["results"]

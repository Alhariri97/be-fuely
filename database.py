from unittest import result
from model import User
import googlemaps
gmaps = googlemaps.Client(key = "AIzaSyCEqKeNPOucSSpZ9MLnchQV-CsvZueN4bQ")


## MongoDB driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://me:mongo@cluster0.ma8gt.mongodb.net/?retryWrites=true&w=majority")
database = client.Petrol
collection = database.users

def get_petrol_stations(lat, lon):
    print(lat, lon, "<<<<<<<<<<<<<<<<<, from database")
    result = gmaps.places( location=(f"{lat}, {lon}"), radius=2, type="gas_station")
    return result["results"]

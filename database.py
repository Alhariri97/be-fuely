import motor.motor_asyncio
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://baldock92:aauab*M6y$PGE8s@cluster0.b0udzos.mongodb.net/?retryWrites=true&w=majority")

database=client.petrol
collection = database.stations

from model import User
import json

from dotenv import load_dotenv
load_dotenv()
import os
apiKey = os.getenv("googleAPIKey")

import googlemaps
gmaps = googlemaps.Client(key = apiKey)

async def get_petrol_stations(lat, lon):
    result = gmaps.places( location=(f"{lat}, {lon}"), radius=2, type="gas_station")

    i=0
    newArr = []
    while i < len(result["results"]):
        newArr.append({"name" : result["results"][i]["name"], "station_id" : result["results"][i]["place_id"], "address" : result["results"][i]["formatted_address"], "coordinates" : {"lat" : result["results"][i]["geometry"]["location"]["lat"], "lng" : result["results"][i]["geometry"]["location"]["lng"]}, "price" : 0, "votes" : 0 })
        i+=1
    
    document = {"example" : str}
    converted = json.dumps({"example": newArr[0]})
    inserting = await collection.insert_one(document)
    return converted
    
    #conditional logic, check if station_id in database already

    



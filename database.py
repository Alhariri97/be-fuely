import motor.motor_asyncio
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://me:mongo@cluster0.ma8gt.mongodb.net/?retryWrites=true&w=majority")

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
import json


async def get_petrol_stations(lat, lon):
    allTheStaionsId = []
    newFromGoogle = []
    result = gmaps.places( location=(f"{lat}, {lon}"), radius=2, type="gas_station")
    i=0
    # print(type(result))
    # return result
    while i < len(result["results"]):
        newFromGoogle.append({ "name" : result["results"][i]["name"], "station_id" : result["results"][i]["place_id"], "address" : result["results"][i]["formatted_address"], "coordinates" : {"lat" : result["results"][i]["geometry"]["location"]["lat"], "lng" : result["results"][i]["geometry"]["location"]["lng"]}, "price" : 0, "votes" : 0 })
        allTheStaionsId.append(result["results"][i]["place_id"])
        i += 1
#####################
    j= 0
    while j < len(newFromGoogle):
        document = await collection.find_one({"station_id" : newFromGoogle[j]["station_id"]})
        if document == None:
            newStationToDataBase = await collection.insert_one(newFromGoogle[j])
        # else:
        #     print( "It's already in your database")
        j += 1
#####################
    d = 0 
    staionsFromDataBase = []
    while d < len(allTheStaionsId):
        document = await collection.find_one({"station_id" : allTheStaionsId[d]})
        staionsFromDataBase.append(document)
        d +=1
    print(type(staionsFromDataBase))

    return(staionsFromDataBase)
    # print(type())
    # print(type(staionsFromDataBase))
    # return staionsFromDsataBase
    # return {"staions":{"d":staionsFromDataBase}, "lon":"any", "lat": "any", "user": "jj"}

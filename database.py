from dotenv import load_dotenv
import os
from fastapi import HTTPException
import googlemaps
import numpy as np
import random
import motor.motor_asyncio
from datetime import datetime
from time import sleep

load_dotenv()
apiKey = os.getenv("googleAPIKey")
DBconnection = os.getenv("PersonalDBConnection") or os.getenv("MONGODB_URL")

gmaps = googlemaps.Client(key=apiKey)
client = motor.motor_asyncio.AsyncIOMotorClient(DBconnection)

database = client.petrol
collection = database.stations
prices = database.prices


def random_price():
    return (random.randrange(190, 210, 1) + 0.9)


def giveDate():
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")


async def get_petrol_stations(lat, lng):
    allTheStationsId = []
    newFromGoogle = []
    try:
        type(float(lat)) == float or type(float(lng)) == float
    except:
        raise HTTPException(status_code=400, detail="Bad Request")
    if float(lat) <= -90 or float(lat) >= 90 or float(lng) <= -180 or float(lng) >= 180:
        raise HTTPException(status_code=404, detail="Not found")
    result = gmaps.places(
        location=(f"{lat}, {lng}"), radius=2, type="gas_station")
    i = 0
    while i < len(result["results"]):
        newFromGoogle.append({"name": result["results"][i]["name"], "station_id": result["results"][i]["place_id"], "address": result["results"][i]["formatted_address"], "coordinates": {
                             "lat": result["results"][i]["geometry"]["location"]["lat"], "lng": result["results"][i]["geometry"]["location"]["lng"]}, "price": [{"price": random_price(), "time_submitted": giveDate(), "user": "default"}], "votes": 0})
        allTheStationsId.append(result["results"][i]["place_id"])
        i += 1
    j = 0
    while j < len(newFromGoogle):
        document = await collection.find_one({"station_id": newFromGoogle[j]["station_id"]})
        if document == None:
            await collection.insert_one(newFromGoogle[j])
        j += 1
    d = 0
    stationsFromDataBase = []
    while d < len(allTheStationsId):
        document = await collection.find_one({"station_id": allTheStationsId[d]})
        stationsFromDataBase.append(document)
        d += 1
    for i in range(len(stationsFromDataBase)):
        del stationsFromDataBase[i]["_id"]
    return(stationsFromDataBase)


async def change_price(price):
    station_id = price.station_id
    petrol_price = price.price
    user = price.user
    if petrol_price <= 180 or petrol_price >= 250:
        raise HTTPException(status_code=400, detail="Bad Request")
    checkForExitstsStation = await collection.find_one({"station_id": station_id})
    if checkForExitstsStation:
        await collection.update_one({"station_id": station_id}, {"$push": {"price": {"price": petrol_price, "time_submitted": giveDate(), "user": user}}})
        updated_station = await collection.find_one({"station_id": station_id})
        del updated_station["_id"]
        return updated_station
    else:
        raise HTTPException(status_code=404, detail="No stations found")

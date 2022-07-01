from dotenv import load_dotenv
import os
from time import sleep
load_dotenv()
apiKey = os.getenv("googleAPIKey")
DBconnection =  os.getenv("PersonalDBConnection") or os.getenv("MONGODB_URL") 

import googlemaps
gmaps = googlemaps.Client(key = apiKey)

import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(DBconnection)





database=client.petrol
collection = database.stations
prices = database.prices
from model import User

import random
def random_price():
    return (random.randrange(190,210,1) + 0.9)

def giveDate():
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")

async def get_petrol_stations(lat, lng):
    twoPageResult = []
    allTheStationsId = []
    newFromGoogle = []
    result =   gmaps.places( location=(f"{lat}, {lng}"), radius=2, type="gas_station")
    twoPageResult.append(result)
    sleep(2)

    nextPage =  gmaps.places( location=(f"{lat}, {lng}"), radius=2, type="gas_station", page_token = result["next_page_token"])
    twoPageResult.append(nextPage)
   
      




    i=0
    while i < len(twoPageResult):
      
        newFromGoogle.append({ "name" : result["results"][i]["name"], "station_id" : result["results"][i]["place_id"], "address" : result["results"][i]["formatted_address"], "coordinates" : {"lat" : result["results"][i]["geometry"]["location"]["lat"], "lng" : result["results"][i]["geometry"]["location"]["lng"]}, "price" : [{ "time_submitted": giveDate(), "price": random_price(),"user":"default"}], "votes" : 0 })
        allTheStationsId.append(result["results"][i]["place_id"])
        i += 1
#####################
    j= 0
    while j < len(newFromGoogle):
        document = await collection.find_one({"station_id" : newFromGoogle[j]["station_id"]})
        if document == None:
            newStationToDataBase = await collection.insert_one(newFromGoogle[j])
        j += 1
        d = 0 
    stationsFromDataBase = []
    while d < len(allTheStationsId):
        document = await collection.find_one({"station_id" : allTheStationsId[d]})
        stationsFromDataBase.append(document)
        d +=1
 
    for i in range(len(stationsFromDataBase)):
        del stationsFromDataBase[i]["_id"]
    return(stationsFromDataBase)



##########################

from datetime import datetime

# now = datetime.now()
# dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
# print(dt_string)
async def change_price(price):
    station_id = price.station_id
    petrol_price = price.price
    user = price.user



    await collection.update_one({"station_id" : station_id},
    
    {"$push" : { "price" : {"price" : petrol_price, "time_submitted": giveDate(), "user" : user} } })

    updated_station = await collection.find_one({"station_id" : station_id})
    del updated_station["_id"]
    return updated_station






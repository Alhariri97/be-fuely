from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import User
import googlemaps
gmaps = googlemaps.Client(key = "AIzaSyCEqKeNPOucSSpZ9MLnchQV-CsvZueN4bQ")
# For the thread function

import time
import threading

start = time.perf_counter()
# End of importing of the thread function

from database import(
    get_petrol_stations
)


app = FastAPI()


origins = ["https:/localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins =origins,
    allow_credentials = True, 
    allow_methods=["*"],
    allow_headers=["*"],
)
import json

@app.get("/")
def read_root():
    return {"hello":"Geo"}

import json

@app.post("/petrol" ,response_model=User ) 
def fetch_petrol_stations(user: User):
    lat = user.lat
    lon = user.lon
    print(lat, lon, "<<<<<<<<<<<<<<<<<, from main")
    response =  get_petrol_stations(lat, lon)
    res = json.dumps(response)
    return {"allStations":res, "lon": lon, "lat": lat}


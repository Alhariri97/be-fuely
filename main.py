from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import (User)

# For the thread function

# End of importing of the thread function

from database import(
    get_petrol_stations,
    # stationsInDataBase
)
#ChIJA-l0qwu7cEgRCYbHFKiqC8A

app = FastAPI()


origins = ["https:/localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins =origins,
    allow_credentials = True, 
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"hello":"Geo"}

import json
# new
@app.post("/petrol" ,response_model=User ) 
async def fetch_petrol_stations(user: User):
    lat = user.lat
    lon = user.lon
    response =  await get_petrol_stations(lat, lon)
    print(type(response))
    return {"allStations":response,  "lon": lon, "lat": lat}





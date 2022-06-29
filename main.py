from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import (User, Price, ReturnPrice)

from database import(
    get_petrol_stations,
    change_price,
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

@app.get("/")
def read_root():
    return {"hello":"Geo"}

import json
# new
@app.post("/stations" ,response_model=User ) 
async def fetch_petrol_stations(user: User):
    lat = user.lat
    lng = user.lng
    response =  await get_petrol_stations(lat, lng)
    return {"allStations":response,  "lng": lng, "lat": lat}

@app.put("/stations/price", response_model=ReturnPrice)
async def update_price(price: Price):
    
    response = await change_price(price)
   
    del response["_id"]
    return {"updated_station": response}

#
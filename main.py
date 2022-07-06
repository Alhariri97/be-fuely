from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import (User, Price, ReturnPrice)
from database import(
    get_petrol_stations,
    change_price,
)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"hello": "Tea(m)418", "Am_I_In_The_Right_Place": "Yes you are, send a lovely request to 'https://fuely.herokuapp.com/api' to get all the avalible end points that team (Tea(m)418) provides! "}


@app.get("/api")
def read_root():
    return {"hello": "Geo"}


app.get("/*")


def read_root():
    raise HTTPException(status_code=404, detail="Not found")


@app.post("/api/stations", response_model=User)
async def fetch_petrol_stations(user: User):
    lat = user.lat
    lng = user.lng
    response = await get_petrol_stations(lat, lng)
    return {"allStations": response,  "lng": lng, "lat": lat}


@app.put("/api/price", response_model=ReturnPrice)
async def update_price(price: Price):

    response = await change_price(price)

    return {"updated_station": response}


@app.get("/api/*")
def read_root():
    return {"Error": "No path!"}

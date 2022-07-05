from http import client
from urllib import response
from fastapi.testclient import TestClient
from httpx import AsyncClient
from main import app
import pytest
import asyncio




# async def test_read_root():
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.get("/")
#     assert response.status_code == 200
#     assert response.json()== {"hello":"Tea(m)418", "Am_I_In_The_Right_Place":"Yes you are, send a lovely request to 'https://fuely.herokuapp.com/api' to get all the avalible end points that team (Tea(m)418) provides! "}



# async def test_read_api():
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.get("/api")
#     assert response.status_code == 200
#     assert response.json()== {"hello":"Geo"}

# async def test_bad_endpoint():
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.get("/blurble")
#     assert response.status_code == 404


# data= {
#   "user": "string",
#   "lng": "-1.0732336",
#   "lat": "54.5937826",
#   "allStations": [
#     "string"
#   ]
# }

# priceData = {  "station_id": "ChIJRcoWwvA8eUgRi7zuN7hWtKA",
#     "user": "andy",
#     "price": 189.9}


# async def test_post_stations():
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.post("/api/stations", json = data)
#     assert response.status_code == 200
#     assert type(response.json() )==dict
#     assert type(response.json()["allStations"] )== list
#     assert type(response.json()["allStations"][0]) == dict
#     for i in range(len(response.json()["allStations"])):
#       assert type(response.json()["allStations"][i]) ==dict
#     for i in range(len(response.json()["allStations"])):
#         assert list(response.json()["allStations"][i].keys()) == ['name', "station_id", "address", "coordinates", "price", "votes"]
#         assert list(response.json()["allStations"][i]["coordinates"].keys()) == ["lat", "lng"]
#         assert type(response.json()["allStations"][i]["coordinates"]["lat"]) == float
#         assert type(response.json()["allStations"][i]["coordinates"]["lng"]) == float
#         assert len(response.json()["allStations"][i]["price"]) >= 1
#         assert list(response.json()["allStations"][i]["price"][0].keys()) == ["price","time_submitted", "user"]
#         for j in range(len(response.json()["allStations"][i]["price"])):
#           assert list(response.json()["allStations"][i]["price"][j].keys()) ==  ["price","time_submitted", "user"]
#           assert type(response.json()["allStations"][i]["price"][j]["time_submitted"]) == str
#           assert type(response.json()["allStations"][i]["price"][j]["price"]) == float
#           assert type(response.json()["allStations"][i]["price"][j]["user"]) == str
#         assert type(response.json()["allStations"][i]["name"]) == str
#         assert type(response.json()["allStations"][i]["station_id"]) == str
#         assert type(response.json()["allStations"][i]["address"]) == str
#         assert type(response.json()["allStations"][i]["coordinates"]) == dict
#         assert type(response.json()["allStations"][i]["price"]) == list
#         assert type(response.json()["allStations"][i]["votes"]) == int


badStationData= {
  "user": "string",
  "lng": "1000000.17403",
  "lat": "41.40338",
  "allStations": [
    "string"
  ]
}

async def test_post_stations_with_error():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/stations", json = badStationData)
    assert response.status_code == 404                


# async def test_put_stations():
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.put("/api/price", json = priceData)
#     assert response.status_code == 200
#     assert type(response.json() )==dict
#     assert type(response.json()["updated_station"]) == dict
#     assert type(response.json()["updated_station"]["name"]) == str
#     assert type(response.json()["updated_station"]["station_id"]) == str
#     assert type(response.json()["updated_station"]["address"]) == str
#     assert type(response.json()["updated_station"]["coordinates"]) == dict
#     assert type(response.json()["updated_station"]["coordinates"]["lat"]) == float
#     assert type(response.json()["updated_station"]["coordinates"]["lng"]) == float
#     assert type(response.json()["updated_station"]["price"]) == list
#     for i in range(len(response.json()["updated_station"]["price"])):
#       assert list(response.json()["updated_station"]["price"][i].keys()) ==  ["price", "time_submitted", "user"]
#       assert type(response.json()["updated_station"]["price"][i]["time_submitted"]) == str
#       assert type(response.json()["updated_station"]["price"][i]["price"]) == float
#       assert type(response.json()["updated_station"]["price"][i]["user"]) == str


import asyncio
from http import client
from urllib import response
from fastapi.testclient import TestClient
import pytest
from httpx import AsyncClient
from main import app
import asyncio
client = TestClient(app, backend="trio",backend_options={"use_uvloop": True})


# def test_root(event_loop):
#     url = "http://test/"
#     resp = event_loop.run_until_complete((url))
#     assert response.status_code ==200


@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(app=app, base_url="http://") as ac:
      response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"hello":"Tea(m)418", "Am_I_In_The_Right_Place":"Yes you are, send a lovely request to 'https://fuely.herokuapp.com/api' to get all the avalible end points that team (Tea(m)418) provides! "}
    assert response.json()["hello"] == "Tea(m)418" 

@pytest.mark.asyncio
async def test_read_api():
  async with AsyncClient(app=app, base_url="http://test") as ac:
    response = await ac.get("/api/")
    assert response.status_code == 200
    assert response.json()== {"hello":"Geo"}

loop = asyncio.get_event_loop()

# @pytest.mark.asyncio
async def test_post_stations():
  data= {
  "user": "string",
  "lng": "-1.0732336",
  "lat": "54.5937826",
  "allStations": [
    "string"
  ]
}
  async with AsyncClient(app=app, base_url="http://test") as ac:
    response = await ac.post("/api/stations", json=data)
    assert response.status_code == 200
#     assert type(response.json() )==dict
    # assert type(response.json()["allStations"] )== list
    # assert type(response.json()["allStations"][0]) == dict
    # for i in range(len(response.json()["allStations"])):
    #   assert type(response.json()["allStations"][i]) ==dict
    # for i in range(len(response.json()["allStations"])):
    #     assert list(response.json()["allStations"][i].keys()) == ['name', "station_id", "address", "coordinates", "price", "votes"]
    #     assert list(response.json()["allStations"][i]["coordinates"].keys()) == ["lat", "lng"]
    #     assert type(response.json()["allStations"][i]["coordinates"]["lat"]) == float
    #     assert type(response.json()["allStations"][i]["coordinates"]["lng"]) == float
    #     assert len(response.json()["allStations"][i]["price"]) >= 1
    #     assert list(response.json()["allStations"][i]["price"][0].keys()) == ["time_submitted", "price", "user"]
    #     for j in range(len(response.json()["allStations"][i]["price"])):
    #       assert list(response.json()["allStations"][i]["price"][j].keys()) ==  ["time_submitted", "price", "user"]
    #       assert type(response.json()["allStations"][i]["price"][j]["time_submitted"]) == str
    #       assert type(response.json()["allStations"][i]["price"][j]["price"]) == float
    #       assert type(response.json()["allStations"][i]["price"][j]["user"]) == str
    #     assert type(response.json()["allStations"][i]["name"]) == str
    #     assert type(response.json()["allStations"][i]["station_id"]) == str
    #     assert type(response.json()["allStations"][i]["address"]) == str
    #     assert type(response.json()["allStations"][i]["coordinates"]) == dict
    #     assert type(response.json()["allStations"][i]["price"]) == list
    #     assert type(response.json()["allStations"][i]["votes"]) == int


# Blocking call which returns when the hello_world() coroutine is done


@pytest.mark.asyncio
async def test_put_station():
  priceData = {  "station_id": "ChIJ7ZAuax4heUgRrhEVajHbwuY",
    "user": "andy",
    "price": 199.9}
  async with AsyncClient(app=app, base_url="http://test") as ac:
    response = await ac.put("/api/price", json=priceData)
    assert response.status_code == 200
#     assert type(response.json() )==dict
    # # assert type(response.json()["updated_station"]) == dict
    # # assert type(response.json()["updated_station"]) == str
    # # assert type(response.json()["updated_station"]["name"]) == str
    # # assert type(response.json()["updated_station"]["station_id"]) == str
    # # assert type(response.json()["updated_station"]["address"]) == str
    # # assert type(response.json()["updated_station"]["coordinates"]) == dict
    # # assert type(response.json()["updated_station"]["coordinates"]["lat"]) == float
    # # assert type(response.json()["updated_station"]["coordinates"]["lng"]) == float
    # # assert type(response.json()["updated_station"]["price"]) == list
    # # for i in range(len(response.json()["updated_station"]["price"])):
    # #   assert list(response.json()["updated_station"]["price"][i].keys()) ==  ["time_submitted", "price", "user"]
    # #   assert type(response.json()["updated_station"]["price"][i]["time_submitted"]) == str
    # #   assert type(response.json()["updated_station"]["price"][i]["price"]) == float
    # #   assert type(response.json()["updated_station"]["price"][i]["user"]) == str


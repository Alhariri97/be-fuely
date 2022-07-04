from http import client
from urllib import response
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()== {"hello":"Tea(m)418", "Am_I_In_The_Right_Place":"Yes you are, send a lovely request to 'https://fuely.herokuapp.com/api' to get all the avalible end points that team (Tea(m)418) provides! "}

def test_read_api():
    response = client.get("/api/")
    assert response.status_code == 200
    assert response.json()== {"hello":"Geo"}

data= {
  "user": "string",
  "lng": "-1.0732336",
  "lat": "54.5937826",
  "allStations": [
    "string"
  ]
}

def test_post_staions():

    response = client.post("/api/stations", json=data)
    assert response.status_code == 200
    assert type(response.json() )==dict
    assert type(response.json()["allStations"] )== list
    assert type(response.json()["allStations"][0]) == dict
    for i in range(len(response.json()["allStations"])):
      assert type(response.json()["allStations"][i]) ==dict
    for i in range(len(response.json()["allStations"])):
        assert list(response.json()["allStations"][i].keys()) == ['name', "station_id", "address", "coordinates", "price", "votes"]
        assert list(response.json()["allStations"][i]["coordinates"].keys()) == ["lat", "lng"]
        assert type(response.json()["allStations"][i]["coordinates"]["lat"]) == float
        assert type(response.json()["allStations"][i]["coordinates"]["lng"]) == float
        assert len(response.json()["allStations"][i]["price"]) >= 1
        assert list(response.json()["allStations"][i]["price"][0].keys()) == ["time_submitted", "price", "user"]
        for j in range(len(response.json()["allStations"][i]["price"])):
          assert list(response.json()["allStations"][i]["price"][j].keys()) ==  ["time_submitted", "price", "user"]
          assert type(response.json()["allStations"][i]["price"][j]["time_submitted"]) == str
          assert type(response.json()["allStations"][i]["price"][j]["price"]) == float
          assert type(response.json()["allStations"][i]["price"][j]["user"]) == str
        assert type(response.json()["allStations"][i]["name"]) == str
        assert type(response.json()["allStations"][i]["station_id"]) == str
        assert type(response.json()["allStations"][i]["address"]) == str
        assert type(response.json()["allStations"][i]["coordinates"]) == dict
        assert type(response.json()["allStations"][i]["price"]) == list
        assert type(response.json()["allStations"][i]["votes"]) == int



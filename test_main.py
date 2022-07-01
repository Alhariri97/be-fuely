from http import client
from urllib import response
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()== {"hello":"Tea(m)418", "I'm_I_In_The_Right_Place":"Yes you are, send a lovely request to 'https://fuely.herokuapp.com/api' to get all the avalible end points that team (Tea(m)418) provides! "}

def test_read_api():
    response = client.get("/api/")
    assert response.status_code == 200
    assert response.json()== {"hello":"Geo"}

def test_post_staions():
    data= {
  "user": "string",
  "lng": "-1.0732336",
  "lat": "54.5937826",
  "allStations": [
    "string"
  ]
}
    response = client.post("/api/stations", json=data)
    assert response.status_code == 200
    assert type(response.json() )==dict
    assert type(response.json()["allStations"] )== list
    assert type(response.json()["allStations"][0]) == dict
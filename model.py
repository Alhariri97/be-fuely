from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    user: Optional[str]
    lng: str
    lat: str
    allStations: Optional[list]


class Price(BaseModel):
    station_id: str
    user: str
    price: float


class ReturnPrice(BaseModel):
    updated_station: dict

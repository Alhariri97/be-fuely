from typing import Optional
from pydantic import BaseModel


# new
class User(BaseModel):
    user: Optional[str]
    lng: str
    lat: str
    # radius: int
    allStations: Optional[list]

class Price(BaseModel):
    station_id: str
    user: str
    price: float
    
class ReturnPrice(BaseModel):
    updated_station: dict





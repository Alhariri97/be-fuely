from typing import Optional
from pydantic import BaseModel



class User(BaseModel):
    user: Optional[str]
    lon: str
    lat: str
    # radius: int
    allStations: Optional[str]


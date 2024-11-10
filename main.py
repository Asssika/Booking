from datetime import date

from fastapi import FastAPI, Query, Depends
from typing import Optional
from pydantic import BaseModel, Field


from users.router import router as router_users
from bookings.router import router as router_bookings

app = FastAPI()


app.include_router(router_users)
app.include_router(router_bookings)


class SearchHotelsARrgs:
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        stars: Optional[int] = Query(None, ge=1, le=5),
        has_spa: Optional[bool] = None,
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.stars = stars
        self.has_spa = has_spa


class Shotel(BaseModel):
    name: str
    address: str
    stars: int = Field(ge=1, le=5)


@app.get("/hotels")
def get_hotels(
            search_args: SearchHotelsARrgs = Depends()
) -> list[Shotel]:
    hotels = {
        'name': 'Anton',
        'address': 'First St.',
        'stars': 4,
    },
    return hotels


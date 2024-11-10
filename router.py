from datetime import date

from fastapi import APIRouter, Request, Depends

from bookings.dao import BookingDAO
from bookings.schemas import SBooking
from users.dependencies import get_current_user
from users.models import Users
from exceptions import RoomCannotBeBooked

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"],
)

@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[dict[str, SBooking]]:
    return await BookingDAO.find_all(user_id=user.id)

@router.post("")
async def add_booking(
        room_id: int, date_from: date, date_to: date,
        user: Users = Depends(get_current_user),
):
    booking = await BookingDAO.add(user.id, room_id, date_from, date_to)
    if not booking:
        raise RoomCannotBeBooked



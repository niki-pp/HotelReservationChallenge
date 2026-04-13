from dataclasses import dataclass, field
from datetime import date
from app.services.util import generate_unique_id, guest_not_found_error
from app.model.hotel import Guest
from datetime import datetime, timedelta, date
from app.services.util import room_not_available_error, reservation_not_found_error


# TODO: Implement Guest class here
@dataclass
class Guest:
    REGULAR = "regular"
    VIP = "vip"

    name: str
    email: str
    type: str = REGULAR

   def __str__(self):
       return f"Guest: {self.name} ({self.email} of type {self.type})"


# TODO: Implement Reservation class here

class Reservation:
    guest_name: str
    description: str
    check_in: date
    check_out: date

    guests: list[Guest] = field(default_factory=list)
    id: str = field(default_factory=generate_unique_id)

    def add_guest(self, name: str, email: str, type_: str = Guest.REGULAR):
        new_guest = Guest(name, email, type_)
        self.guests.append(new_guest)

    def delete_guest(self, guest_index: int):
        if 0 <= guest_index < len(self.guests):
            self.guests.pop(guest_index)
        else:
            guest_not_found_error()

    def __len__(self):
        return (self.check_out - self.check_in).days

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Guest: {self.guest_name}\n"
            f"Description: {self.description}\n"
            f"Dates: {self.check_in} - {self.check_out}"
        )

# TODO: Implement Room class here

class Room:
    def __init__(self, number: int, type_: str, price_per_night: float):
        self.number = number
        self.type_ = type_
        self.price_per_night = price_per_night
        self.availability: dict[date, str | None] = {}
        self._init_availability()

    def _init_availability(self):
        today = datetime.now().date()

        for i in range(365):
            current_day = today + timedelta(days=i)
            self.availability[current_day] = None

# TODO: Implement Hotel class here

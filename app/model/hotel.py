from dataclasses import dataclass, field
from datetime import date
from app.services.util import generate_unique_id, guest_not_found_error
from app.model.hotel import Guest


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

# TODO: Implement Room class here


# TODO: Implement Hotel class here

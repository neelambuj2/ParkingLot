from enum import Enum


class Command(Enum):
    """
    This class Command extending Enum contains the string commands and their Constant Values
    """
    CREATE_PARKING_LOT = "create_parking_lot"
    PARK = "park"
    LEAVE = "leave"
    STATUS = "status"
    REG_NUMBER_FOR_CARS_WITH_COLOR = "registration_numbers_for_cars_with_colour"
    SLOTS_NUMBER_FOR_CARS_WITH_COLOR = "slot_numbers_for_cars_with_colour"
    SLOTS_NUMBER_FOR_REG_NUMBER = "slot_number_for_registration_number"

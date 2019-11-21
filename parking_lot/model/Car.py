from interface.Abstract_vehicle import Vehicle
from enum_constants.vehicle_type import VehicleType


class Car(Vehicle):
    """
    This class extends vehicle class, with properties of a car
    """
    def __init__(self, reg_no, color):
        super().__init__(reg_no=reg_no, color=color, vehicle_type=VehicleType.CAR)


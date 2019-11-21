from abc import ABC


class Vehicle(ABC):
    """
    Thid class is an abstract class which will be inherited by vehicles of type car
    or any other type in future
    """
    def __init__(self, reg_no, color, vehicle_type):
        self.registration_no = reg_no
        self.color = color
        self.type = vehicle_type

from abc import ABC, abstractmethod


class ParkingLotDao(ABC):
    """
    This class contains interfaces for all the parking lot features.Concrete class should
    implement this interface
    """

    @abstractmethod
    def park_vehicle(self, vehicle):
        pass

    @abstractmethod
    def unpark_vehicle(self, slot_id):
        pass

    @abstractmethod
    def print_status(self):
        pass

    @abstractmethod
    def get_reg_no_by_color(self, color):
        pass

    @abstractmethod
    def get_slot_no_by_color(self, color):
        pass

    @abstractmethod
    def get_slot_no_by_reg_no(self, reg_no):
        pass


from collections import defaultdict
from heapq import heappush, heappop
from dao.parking_lot_dao import ParkingLotDao
from interface.Abstract_vehicle import Vehicle
from model.ParkingSpot import ParkingSpot


class ParkingLot(ParkingLotDao):
    """
    This class represents a parking lot with specified number of spots.This class is
    a singleton class because only one instance of parking lot should be there as of now.
    """
    __slot_id = 1
    __parking_lot_instance = None

    def __init__(self, size):
        """
        This is ParkingLot constructor.It initialises the parking lot class with the
        specified number of spots(ie objects of class ParkingSpot).If Parking lot is already
        initialised then it raises an exception with message that parking lot is already created.
        It uses min heap to store the vacant parking spots, so that nearest vacant spots can be
        allocated easily.

        :param size: Number of parking spots required in parking lot
        :return : Parking lot instance
        """
        if ParkingLot.__parking_lot_instance is None:
            self.slots = list()
            for count in range(1, size + 1):
                spot_obj = ParkingSpot(ParkingLot.__slot_id)
                ParkingLot.__slot_id += 1
                heappush(self.slots, spot_obj)
            ParkingLot.__slot_id = size
            ParkingLot.__parking_lot_instance = self
            self.parking_arrangement = dict()
            self.parked_car_hash = dict()
            self.color_hash = defaultdict(list)
            print("Created a parking lot with", size, "slots")

        else:
            raise Exception("Parking lot already created")

    def get_nearest_parking_spot(self):
        """
        It pops the vacant slot which is of min heap type, by default it returns the nearest
        vacant slots since it is min heap.It takes O(1) time.

        :return: nearest vacant parking slot
        """
        if self.slots:
            return heappop(self.slots)
        else:
            raise Exception("Sorry, parking lot is full")

    def restore_parking_spot(self, vacated_slot):
        """
        This function inserts the vacated parking slot in the slot heap.It takes O(logn) time.
        where n is the number of vacant slots in the slot heap.
        :param vacated_slot: The slot which just got vacated.
        """
        heappush(self.slots, vacated_slot)

    def park_vehicle(self, vehicle: Vehicle):
        if vehicle.registration_no not in self.parked_car_hash:
            spot = self.get_nearest_parking_spot()
            self.parking_arrangement[spot.slot_id] = (vehicle, spot)
            self.parked_car_hash[vehicle.registration_no] = spot.slot_id
            ack = "Allocated slot number: %s" % spot.slot_id
            self.color_hash[vehicle.color.lower()].append(vehicle)
            return ack
        else:
            raise Exception("Cars with duplicate registration number cannot be parked")

    def unpark_vehicle(self, slot_id):
        try:
            slot_id = int(slot_id)
        except Exception as e:
            raise Exception("Invalid slot number")
        if slot_id <= 0 or slot_id > ParkingLot.__slot_id:
            raise Exception("Invalid slot number")
        if slot_id in self.parking_arrangement:
            unparked_vehicle, vacated_spot = self.parking_arrangement.pop(slot_id)
            self.parked_car_hash.pop(unparked_vehicle.registration_no)
            self.restore_parking_spot(vacated_spot)
            co_color_vehicle = self.color_hash[unparked_vehicle.color.lower()]
            co_color_vehicle.remove(unparked_vehicle)
            ack = "Slot number %s is free" % slot_id
            return ack
        else:
            raise Exception("This slot is already free")

    def print_status(self):
        print("%-11s %-18s %-0s" % ("Slot No.", "Registration No", "Colour"))
        for slot in self.parking_arrangement.keys():
            print("%-11s %-18s %-0s" % (slot, self.parking_arrangement[slot][0].registration_no,
                  self.parking_arrangement[slot][0].color))

    def get_reg_no_by_color(self, color):
        co_color_vehicle = self.color_hash[color.lower()]
        result = list()
        for vehicle in co_color_vehicle:
            result.append(vehicle.registration_no)
        return result

    def get_slot_no_by_color(self, color):
        co_color_reg_no = self.get_reg_no_by_color(color)
        result = list()
        for reg_no in co_color_reg_no:
            result.append(self.parked_car_hash[reg_no])
        return result

    def get_slot_no_by_reg_no(self, reg_no):
        return self.parked_car_hash.get(reg_no, "Not found")

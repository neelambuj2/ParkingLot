import unittest
from dao.dao_factory import get_in_memory_dao, DaoType
from model.Car import Car
SIZE = 2


class TestParkingLot(unittest.TestCase):
    """
    This class contains the test case for the code.
    setupClass will run once before initialization of unitests tests.
    """

    @classmethod
    def setUpClass(cls):
        """
        This setUp method initialises the Parking lot class with a given size
        """
        cls.parking_lot_obj = get_in_memory_dao(DaoType.in_memory_dao, SIZE)

    def test_parking_lot_is_singleton(self):
        """
        This test tries to initialise the ParkingLot class again to check if it raises exception
        or not.It should raise exception as ParkingLot is already initialised in setUp.
        """

        self.assertRaises(Exception, get_in_memory_dao, DaoType.in_memory_dao, SIZE)

    def test_parking_lot_gets_nearest_parking_spot(self):
        """
        This test tries to get two spot and checks if they are nearest or not,Then it restores
        the spot1 and then again tries to get the nearest spot which should be spot1 now.
        :return:
        """
        spot1 = self.parking_lot_obj.get_nearest_parking_spot()
        self.assertEqual(1, spot1.slot_id)
        self.parking_lot_obj.restore_parking_spot(spot1)
        nearest_spot = self.parking_lot_obj.get_nearest_parking_spot()
        self.assertEqual(1, nearest_spot.slot_id)
        self.parking_lot_obj.restore_parking_spot(spot1)

    def test_simple_parking(self):
        car = Car(reg_no="123A", color="Silver")
        ack = self.parking_lot_obj.park_vehicle(car)
        self.assertTrue(ack, "Allocated slot number: 1")
        self.parking_lot_obj.unpark_vehicle(1)

    def test_parking_same_car_twice(self):
        car = Car(reg_no="123A", color="Silver")
        ack = self.parking_lot_obj.park_vehicle(car)
        self.assertTrue(ack.startswith("Allocated slot number"))
        self.assertRaises(Exception, self.parking_lot_obj.park_vehicle, car)
        self.parking_lot_obj.unpark_vehicle(1)

    def test_get_slot_by_vehicle_reg_no(self):
        car1 = Car(reg_no="231A", color="Black")
        car2 = Car(reg_no="563A", color="White")
        self.parking_lot_obj.park_vehicle(car1)
        self.parking_lot_obj.park_vehicle(car2)
        self.assertEqual(self.parking_lot_obj.get_slot_no_by_reg_no("231A"), 1)
        self.assertEqual(self.parking_lot_obj.get_slot_no_by_reg_no("INVALID"), "Not found")
        self.parking_lot_obj.unpark_vehicle(1)
        self.parking_lot_obj.unpark_vehicle(2)

    def test_unpark_vacant_slot_and_invalid_slot(self):
        self.assertRaises(Exception, self.parking_lot_obj.unpark_vehicle, 2)
        self.assertRaises(Exception, self.parking_lot_obj.unpark_vehicle, "Invalid2")

    def test_get_slot_and_reg_no_by_color(self):
        car2 = Car(reg_no="231A", color="Black")
        car3 = Car(reg_no="563A", color="Black")
        self.parking_lot_obj.park_vehicle(car2)
        self.parking_lot_obj.park_vehicle(car3)
        res = self.parking_lot_obj.get_reg_no_by_color("Black")
        self.assertEqual(res, ['231A', '563A'])
        slot = self.parking_lot_obj.get_slot_no_by_color("Black")
        self.assertEqual(slot, [1, 2])
        self.parking_lot_obj.unpark_vehicle(1)
        self.parking_lot_obj.unpark_vehicle(2)

    def test_parking_lot_full(self):
        car1 = Car(reg_no="231A", color="Black")
        car2 = Car(reg_no="563A", color="Black")
        self.parking_lot_obj.park_vehicle(car1)
        self.parking_lot_obj.park_vehicle(car2)
        car4 = Car(reg_no="897A", color="white")
        self.assertRaises(Exception, self.parking_lot_obj.park_vehicle, car4)
        self.parking_lot_obj.unpark_vehicle(1)
        self.parking_lot_obj.unpark_vehicle(2)


if __name__ == '__main__':
    unittest.main()

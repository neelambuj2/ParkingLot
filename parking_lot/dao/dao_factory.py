from enum import Enum
from dao.in_memory_dao.ParkingLot import ParkingLot
from dao.parking_lot_dao import ParkingLotDao


class DaoType(Enum):
    """
    DAOTypes Enum
    """
    in_memory_dao = ParkingLot


def get_in_memory_dao(daotypes: DaoType, size):
    """
    Method for getting parking lot dao
    :param daotypes: DAOTypes
    :return: parkinglot_dao
    """
    try:
        size = int(size)
    except Exception as e:
        raise Exception("Invalid size of Parking lot")
    parking_lot_dao = daotypes.value(size)
    return parking_lot_dao

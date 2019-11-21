from enum_constants.commands import Command
from model.Car import Car
from dao.dao_factory import get_in_memory_dao, DaoType


class InputManager:
    """
    This class manages the input commands given to the system
    """
    def __init__(self):
        self.parking_lot_obj = None

    def process_input(self, input_str):
        """
        This function compares the input string against a set of enum commands else ignores.
        :param input_str: input command
        """
        splitted_input = input_str.split(" ")
        instruction = splitted_input[0]
        if instruction == Command.CREATE_PARKING_LOT.value:
            if len(splitted_input) == 2:
                self.parking_lot_obj = get_in_memory_dao(DaoType.in_memory_dao, splitted_input[1])

        elif instruction == Command.PARK.value:
            if self.parking_lot_obj and len(splitted_input) == 3:
                car_obj = Car(reg_no=splitted_input[1], color=splitted_input[2])
                ack = self.parking_lot_obj.park_vehicle(car_obj)
                print(ack)

        elif instruction == Command.LEAVE.value:
            if self.parking_lot_obj and len(splitted_input) == 2:
                ack = self.parking_lot_obj.unpark_vehicle(splitted_input[1])
                print(ack)
        elif instruction == Command.STATUS.value:
            if self.parking_lot_obj and len(splitted_input) == 1:
                self.parking_lot_obj.print_status()

        elif instruction == Command.REG_NUMBER_FOR_CARS_WITH_COLOR.value:
            if self.parking_lot_obj and len(splitted_input) == 2:
                result = self.parking_lot_obj.get_reg_no_by_color(splitted_input[1])
                print(", ".join(result))

        elif instruction == Command.SLOTS_NUMBER_FOR_CARS_WITH_COLOR.value:
            if self.parking_lot_obj and len(splitted_input) == 2:
                result = self.parking_lot_obj.get_slot_no_by_color(splitted_input[1])
                result = list(map(lambda x: str(x), result))
                print(", ".join(result))

        elif instruction == Command.SLOTS_NUMBER_FOR_REG_NUMBER.value:
            if self.parking_lot_obj and len(splitted_input) == 2:
                result = self.parking_lot_obj.get_slot_no_by_reg_no(splitted_input[1])
                print(result)






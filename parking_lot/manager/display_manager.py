class DisplayManager:
    """
    This class manages the display of commands
    """

    def print_instructions(self):
        """
        This function prints the input commands for use.
        """
        instructions = list()
        instructions.append("\n--------------Please Enter one of the below commands."
                            " {variable} to be replaced -----------------------")
        instructions.append("1) Create a parking lot of a size                  "
                            " --- create_parking_lot {capacity}")
        instructions.append("2) park a car                                       "
                            "--- park <<car_number>> {car_clour}")
        instructions.append("3) Unpark a car from parking                        "
                            "--- leave {slot_number}")

        instructions.append("4) Print status of parking slot                     "
                            "--- status")
        instructions.append("5) Get cars registration no for the given car color "
                            "--- registration_numbers_for_cars_with_color {car_color}")

        instructions.append("6) Get slot numbers for the given car color         "
                            "--- slot_numbers_for_cars_with_color {car_color}")
        instructions.append("7) Get slot number for the given car number        "
                            " --- slot_number_for_registration_number {car_number}")

        for line in instructions:
            print(line)

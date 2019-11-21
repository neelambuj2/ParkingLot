import sys
from manager.display_manager import DisplayManager
from manager.input_manager import InputManager


class Main:
    """
    This is the main class which runs the program
    """

    def __init__(self):
        self.display_mang = DisplayManager()
        self.input_mang = InputManager()

    def interactive_run(self):
        """
        This method runs the program in interactive mode
        """
        while True:
            try:
                #self.display_mang.print_instructions()
                input_string = input()
                if input_string == "exit":
                    break
                self.input_mang.process_input(input_string)
            except Exception as e:
                print(e)

    def file_input_run(self, filename):
        """
        This method runs the program in file input mode
        :param filename: correct path/{name} of the file. path should be relative to
                         the top parking_lot directory.
        """
        file = open(filename)
        file_content = file.read()
        content_list = file_content.split("\n")
        for command in content_list:
            if command == "exit":
                break
            try:
                self.input_mang.process_input(command)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    arg = sys.argv
    if len(arg) == 2:
        file_name = arg[1]
        Main().file_input_run(file_name)
    elif len(arg) == 1:
        Main().interactive_run()

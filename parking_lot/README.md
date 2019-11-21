Tested on Ubuntu 18.04

To Run the Unit Test and Ruby Tests
make bin/set executable by giving following command:
     "chmod +x bin/setup"
then run set from root by giving following command
     "bin/setup" 
Note: Make sure you have sudo access and run "bin/setup" from top most "parking_lot" dir
Setup will perform the following task
 
1 > setup will install the python dependencies
2 > setup will run the Unit tests (There are 8 Unit tests which contain multiple test checks)
3 > After running unit test setup will run the program and it will give a input file
    using the following command
4 > Output for the input file will be printed on the console
5 > It will install Ruby and related dependencies.
6 > Enter Y if prompted to confirm installation
7 > It will start the Ruby test Suite which has (10 test)
8 > It will print the result to the console

Additionally you can run "bin/parking_lot" to run program in interactive mode.
Total 18 tests will be executes by "setup" along with console output for the input file.

********************************************************************************************


Some information about the code:

1 > To implement the allocation of Nearestparkingspot it uses Min heap.
2 > Commands are stored in Enum constants.
3 > To see the the command instruction, You can uncomment this line 
    "self.display_mang.print_instructions()" in main.py. It is commented because
    automation test are performed.
4 > Actual implementation of the Parking lot functionality can be found here
    "dao/in_memory_dao/ParkingLot.py".
5 > Above file is not directly used but via an abstract class "dao/parking_lot_dao.py".
    inmemory dao has implemented the above abstract class.
6 > The model for vehicle and parking spot can be found under model class and common interface
    for all vehicles to be implemented is here "interface/Abstract_vehicle.py".
7 > There is manager directory, which has input manager which takes care of processing 
    input commands and a display manager which takes care of displaying instructions.
8 > In test folder we have the unit tests whose coverage is around 94%.


for any clarifications
you can reach out to me here : 
Neelambuj
neelambuj2@gmail.com
9944138099
    






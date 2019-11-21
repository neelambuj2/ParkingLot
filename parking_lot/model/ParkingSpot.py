class ParkingSpot:
    """
    This class represents a parking spot in the parking lot.
    IF required more properties can be added to a spot from here
    """
    def __init__(self, slot_id):
        self.slot_id = slot_id

    def __lt__(self, other):
        return self.slot_id < other.slot_id

    def __repr__(self):
        return str(self.slot_id)


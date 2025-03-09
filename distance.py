import datetime

class Distance:
    """
    Class to represent a distance measurement with timestamp.
    """
    def __init__(self, distance):
        """Initialize the Distance object with distance and timestamp."""
        self.distance = distance # get distance as provided
        self.time = datetime.datetime.now() # get timestamp

    def __str__(self):
        """Return a formatted string representation of the Distance object."""
        return f"Distance of {self.distance} taken at {self.time}" # return formatted string

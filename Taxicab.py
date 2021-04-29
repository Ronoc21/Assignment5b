#Name: Conor Smith
#Date: 04/28/2021
#Description: A class that creates an object called Taxicab, places it on a graph with the ability to move the cab by units by adding or subtracting X and Y coordinates

class Taxicab:
    """Created class Taxicab, defines x/ y coordinates and the "odometer" or number of units the cab has moved"""
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self.odometer = 0

    def get_x_coord(self):
        return self._x
    def get_y_coord(self):
        return self._y

    def get_odometer(self):
        return self.odometer

    def move_x(self, distance):
        """how far cab goes left or right"""
        self._x += distance
        self.odometer +=abs(distance)

    def move_y(self, distance):
        """move cab up/down"""
        self._y += distance
        self.odometer +=abs(distance)

cab = Taxicab(5, -8)  # creates a Taxicab object at coordinates (5, -8)
cab.move_x(3)  # moves cab 3 units "right"
cab.move_y(-4)  # moves cab 4 units "down"
cab.move_x(-1)  # moves cab 1 unit "left"
print(cab.get_odometer())
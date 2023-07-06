from python.day15.Point import Point


class Sensor:
    def __init__(self, position: Point, reading: Point):
        self._position = position
        self._reading = reading

    def __str__(self):
        return "position: {}, reading: {}".format(str(self._position), str(self._reading))

    def get_reading(self):
        return self._reading

    def get_position(self):
        return self._position

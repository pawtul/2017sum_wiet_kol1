class Plane(object):
    correct_position = 0

    def __init__(self, correct_position=None):
        if correct_position is not None:
            self.correct_position = correct_position
        self.position = self.correct_position

    def apply_tilt(self, tilt):
        self.position += tilt

    def correct_flight(self):
        diff = abs(self.position - self.correct_position)
        self.position = self.correct_position
        return diff



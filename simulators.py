import random


class PlaneSimulator(object):
    def __init__(self, plane):
        self.plane = plane

    def generate_tilt(self):
        tilt = random.gauss(0, 1)
        if -45 < tilt < 45:
            return tilt
        return self.generate_tilt()

    def __iter__(self):
        while True:
            print "=" * 40
            print "Plane has position: {}".format(self.plane.position)
            tilt = self.generate_tilt()
            print "Applying tilt: {}".format(tilt)
            self.plane.apply_tilt(tilt)
            print "Current plane's position: {}".format(self.plane.position)
            print "Correcting plane's position"
            self.plane.correct_flight()
            print "Current plane's position: {}".format(self.plane.position)
            yield tilt

    def teardown(self):
        print "Simulation Finishes"


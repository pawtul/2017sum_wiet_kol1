from collections import OrderedDict
import random
import time


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


class StopCLI(Exception):
    pass


class CLI(object):
    def __init__(self, namespace=None):
        self.namespace = namespace or {}
        self.commands = OrderedDict([
                ('?', self.help),
                ('help', self.help),
                ('example', self.example),
                ('plane', self.plane),
                ('simulator', self.simulator),
                ('run', self.run),
                ('exit', self.exit),
                ('q', self.exit)
                ])
        self._spawn_cli()

    def _spawn_cli(self):
        print "type help or ? for help"
        while True:
            try:
                command = raw_input("$")
                self._parse_command(command)
            except StopCLI:
                break

    def _parse_command(self, command):
        if not command:
            return
        words = command.split()
        command, args = words[0], words[1:]
        try:
            return self.commands.get(command)(*args)
        except TypeError:
            print "wrong command {}".format(command)

    def example(self, *args):
        """
        prints example usage
        """
        print "type following commands:"
        print "plane"
        print "simulator"
        print "run"

    def run(self, *args):
        """
        runs simulation
        """
        if 'simulator' not in self.namespace:
            self.simulator()
        simulator = self.namespace['simulator']
        print "hit ^C to break\n"
        try:
            for s in simulator:
                time.sleep(0.7)
        except KeyboardInterrupt:
            simulator.teardown()

    def plane(self, correct_pos=None, *args):
        """
        args: [correct_pos] - creates a plane with\
 correct position set to correct_pos
        """
        try:
            position = float(correct_pos)
        except TypeError:
            position = 0
        self.namespace['plane'] = Plane(position)

    def simulator(self, *args):
        """
        creates new simulator
        """
        self.namespace['simulator'] = PlaneSimulator(
                self.namespace.setdefault('plane', Plane()))

    def help(self, command=None, *args):
        """
        args: [command] - prints help
        """
        if command is not None:
            print self.commands.get(command).__doc__
        else:
            for command in self.commands:
                print "{} {}".format(
                        command,  self.commands.get(command).__doc__)

    def exit(self, *args):
        """
        terminates program
        """
        raise StopCLI()


if __name__ == '__main__':
    CLI()


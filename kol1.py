import random
import time


def generate_tilt():
    tilt = random.gauss(0, 1)
    if  -45 < tilt < 45:
	      return tilt
    return generate_tilt()


def compute_correction(orientation):
    return -orientation


ORIENTATION = 0


if __name__ == "__main__":
    while True:
        try:
	          tilt = generate_tilt()
	          print "new tilt is: ", tilt
	          ORIENTATION += tilt
	          print "current orientation: ", ORIENTATION, " degree"

	          correction = compute_correction(ORIENTATION)
	          print "tilt correction: ", correction, " degree"

	          ORIENTATION += correction
	          print "corrected orientation is now: ", ORIENTATION
	          print "=" * 20
	          time.sleep(1.5)
        except KeyboardInterrupt:
	          print "\rleaving"
	          break

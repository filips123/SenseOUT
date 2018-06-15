from sense_hat import SenseHat
import sys

sense = SenseHat()

while True:
    with open(sys.argv[1] if len(sys.argv) > 1 else 'sensehat', 'r') as input:
       for line in input:
           sense.show_message(str(line.strip()))
        
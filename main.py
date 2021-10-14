##The code for calculating spo2 (hrcalc.py) and initializing max30102 (max30102.py) originally comes from vrano714:
##https://github.com/vrano714/max30102-tutorial-raspberrypi
##But with a few modifications so that it won't return ZeroDivisionError

##The code for initializing HeartRateMonitor (heartrate_monitor.py) and main file (main.py) originally comes from doug-burrell:
##https://github.com/doug-burrell/max30102/blob/master/heartrate_monitor.py
##But with a few modifications so that it can be connected to Adafruit IO and Gmail

##The original code is written to run on Arduino Uno:
##https://github.com/MaximIntegratedRefDesTeam/RD117_ARDUINO/

from heartrate_monitor import HeartRateMonitor
import time
import argparse

parser = argparse.ArgumentParser(description="Read and print data from MAX30102")
parser.add_argument("-r", "--raw", action="store_true",
                    help="print raw data instead of calculation result")
parser.add_argument("-t", "--time", type=int, default=30,
                    help="duration in seconds to read from sensor, default 30")
args = parser.parse_args()

print('sensor starting...')
hrm = HeartRateMonitor(print_raw=args.raw, print_result=(not args.raw))
hrm.start_sensor()
try:
    time.sleep(args.time)
except KeyboardInterrupt:
    print('keyboard interrupt detected, exiting...')

hrm.stop_sensor()
print('sensor stoped!')

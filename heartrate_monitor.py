##The code for calculating spo2 (hrcalc.py) and initializing max30102 (max30102.py) originally comes from vrano714:
##https://github.com/vrano714/max30102-tutorial-raspberrypi
##But with a few modifications so that it won't return ZeroDivisionError

##The code for initializing HeartRateMonitor (heartrate_monitor.py) and main file (main.py) originally comes from doug-burrell:
##https://github.com/doug-burrell/max30102/blob/master/heartrate_monitor.py
##But with a few modifications so that it can be connected to Adafruit IO and Gmail

##The original code is written to run on Arduino Uno:
##https://github.com/MaximIntegratedRefDesTeam/RD117_ARDUINO/

import max30102
import hrcalc
import time
import numpy as np
from Adafruit_IO import *

m = max30102.MAX30102()
IO_USERNAME = "Your Username"
IO_KEY = "Your Key"
bpm_key = "max30102_bpm"
spo2_key = "max30102_spo2"
threshold_key = "max30102_threshold"


class HeartRateMonitor(object):

    LOOP_TIME = 0.01

    def __init__(self, print_raw=False, print_result=False):
        self.bpm = 0
        if print_raw is True:
            print('IR, Red')
        self.print_raw = print_raw
        self.print_result = print_result
        self.rec_bpm = []
        self.rec_spo2 = []
        self.avg_bpm = 0
        self.avg_spo2 = 0

    def run_sensor(self):
        sensor = MAX30102()
        ir_data = []
        red_data = []
        bpms = []
        aio = Client(IO_USERNAME, IO_KEY)
        i = 0
        abn = 0

        # run until told to stop
        while not self._thread.stopped:
            # check if any data is available
            num_bytes = sensor.get_data_present()
            i += 1
            if num_bytes > 0:
                # grab all the data and stash it into arrays
                while num_bytes > 0:
                    red, ir = sensor.read_fifo()
                    num_bytes -= 1
                    ir_data.append(ir)
                    red_data.append(red)
                    if self.print_raw:
                        print("{0}, {1}".format(ir, red))

                while len(ir_data) > 100:
                    ir_data.pop(0)
                    red_data.pop(0)

                if len(ir_data) == 100:
                    bpm, valid_bpm, spo2, valid_spo2 = hrcalc.calc_hr_and_spo2(ir_data, red_data)
                    if valid_bpm:
                        bpms.append(bpm)
                        while len(bpms) > 4:
                            bpms.pop(0)
                        self.bpm = np.mean(bpms)
                        if (np.mean(ir_data) < 50000 and np.mean(red_data) < 50000):
                            self.bpm = 0
                            if self.print_result:
                                print("Finger not detected")
                        if self.print_result:
                            self.rec_bpm.append(self.bpm)
                            if spo2 >= 80:
                                self.rec_spo2.append(spo2)
                            else:
                                abn += 1
                            print("BPM: {0}, SpO2: {1}".format(self.bpm, spo2))
                            if i % 30 == 0:
                                aio.send(bpm_key, self.bpm)
                                aio.send(spo2_key, spo2)
                                
        
            time.sleep(self.LOOP_TIME)

        aio.send(threshold_key, abn/i)
        sensor.shutdown()

    def start_sensor(self):
        self._thread = threading.Thread(target=self.run_sensor)
        self._thread.stopped = False
        self._thread.start()

    def stop_sensor(self, timeout=2.0):
        self._thread.stopped = True
        self.bpm = 0
        self._thread.join(timeout)
        print("Average BPM:{0}, Average SpO2:{1}".format(self.avg_bpm, self.avg_spo2))
        if self.avg_spo2<90 and (self.avg_bpm <60 or self.avg_bpm>100):
            print("DANGER!!")
        aio.send(bpm_key, self.avg_bpm)
        aio.send(spo2_key, self.avg_spo2)
        self.bpm = 0
        self.rec_bpm = []
        self.rec_spo2 = []
        self.avg_bpm = 0
        self.avg_spo2 = 0
        self._thread.join(timeout)

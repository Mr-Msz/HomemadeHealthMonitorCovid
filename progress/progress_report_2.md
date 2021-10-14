## Current Progress - 10/04/2021

### Update
With the help of a Github repo of the package of MAX30100/02 and our code, the sensor is finally light up, we are able to get bpm and oxygen saturation at the same time. We believe the sampling frequency makes the data abnormal, so it will be tuned in the coming week. At the same time, we started to look into LCD output.
<p align="center">
    <img src="https://github.com/Mr-Msz/HomemadeHealthMonitorCovid/blob/main/Figure/Output-10-04-2021.png?raw=true"/>
</p>

### Problems Encountered
It seems like although the sensor indicates its voltage level to be 3.3V, in order to light it, we will need to connect it to 5V. Another problem we encountered is that if the sampling frequency is too high, the sensors ends up outputting strange data (150 BPM —> 60 BPM —> 150 BPM in one second).

### Future Plan
If we can’t maintain the stability with high sampling frequency, we will reduce that to a lower level. By connecting it to an output device, the data visualization will be mostly done. If time is enough, we can upload the data to online data storage with the help of IOT.

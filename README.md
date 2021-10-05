## Homemade Health Monitoring Device for Covid-19

### Video Link



### Introduction
Write a brief summary of your project

### Motivation
Motivate the problem you plan to address

Why is the problem you are addressing important or interesting?

### Goals
What are you going to achieve by the end of the project specifically?

## Progress Report (Last Update 10/04/2021)
### Current Progress
#### Update - 10/04/2021
With the help of a Github repo of the package of MAX30100/02 and our code, the sensor is finally light up, we are able to get bpm and oxygen saturation at the same time. Next part will be working on outputting the data and revise codes.

![Image of BPM&SpO2](https://github.com/Mr-Msz/HomemadeHealthMonitorCovid/blob/main/Figure/Output-10-04-2021.png?raw=true)

#### Update - 10/02/2021
We received our MAX30102 and began to work on the hardware part of the project. We prepare to work on the paper simultaneously in case we encounter some difficult situation later.
#### Update - 09/30/2021
Instead of making a sensor ourselves and try to compare with the state-of-art, we decide to be more realistic on our goals. Still, we will use MAX30102 as our main sensor. At the same time, we will try to put it together with Raspberry Pi which is not its originally intended platform. If time is enough, we will try to compare its characteristics with some oximeter on market. For the self-reported part of the device, after reading some related materials, we decide to change it to a device that is visualizable and can be used as a self-check measure for users. This will require a 16x2 LCD to perform.

### Problems Encountered
#### Update - 10/04/2021
It seems like although the sensor indicates its voltage level to be 3.3V, in order to light it, we will need to connect it to 5V. Another problem we encountered is that if the sampling frequency is too high, the sensors ends up outputting strange data (150 BPM —> 60 BPM —> 150 BPM in one second).
#### Update - 10/02/2021
As MAX30102 is not originally produced for Raspberry Pi, we encountered with a problem of how to light the sensor up. Because of its compatibility, the official code seems to be not working. We will need a package for MAX30102 for Raspberry Pi.

### Future Plan
#### Update - 10/04/2021
If we can’t maintain the stability with high sampling frequency, we will reduce that to a lower level. By connecting it to an output device, the data visualization will be mostly done. If time is enough, we can upload the data to online data storage with the help of IOT.

## Methodology
### Phenomena of Interest
We hope to measure 

### Sensor(s) Used

### Signal Conditioning and Processing

## Experiments and Results
### Code
```markdown
#### Coding Part
```

## Discussion


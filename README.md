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
With the help of a Github repo of the package of MAX30100/02 and our code, the sensor is finally light up, we are able to get bpm and oxygen saturation at the same time. We believe the sampling frequency makes the data abnormal, so it will be tuned in the coming week. At the same time, we started to look into LCD output.
<p align="center">
    <img src="https://github.com/Mr-Msz/HomemadeHealthMonitorCovid/blob/main/Figure/Output-10-04-2021.png?raw=true"/>
</p>

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
In this project, we hope to measure oxygen saturation and heart rate as the indicators to see if the user is at risk of COVID-19 or other diseases.

#### Oxygen Saturation
Oxygen saturation, or "O2 sats," indicates that amount of oxygen traveling through your body with your red blood cells. Blood disorders, problems with circulation, and lung issues may prevent the body from absorbing or transporting enough oxygen. In turn, that can lower your blood's oxygen saturation level.[1]¬ Therefore, oxygen saturation is useful for detecting multiple abnormal conditions including respiratory infections (e.g. a cold, the flu, COVID-19), chronic obstructive pulmonary disease (COPD), asthma, heart disease, etc. 

During pandemic, oxygen pandemic seems more useful. Research has shown that some people with COVID-19 have dangerously low levels of oxygen. Dr. Bime, a critical care medicine specialist with a focus in pulmonology at Banner - University Medical Center Tucson, suggested that If you’ve been exposed to COVID-19, or you’ve tested positive and develop symptoms, you had better check your oxygen saturation. If it’s low or you notice it’s dropping, contact your healthcare provider.[2]

Oxygen saturation is such an important index of health, not only because it’s obviously influenced by the abnormal body conditions, but also due to the easy way to measure. Oxygen saturation is usually measured one of two ways: arterial blood gas test (ABG or SaO2) and pulse oximetry (SpO2). [1]¬ Usually, we use SpO2 to describe the oxygen saturation, which reflects the percentage of oxygen found in arterial blood. The test uses a sensor to read wavelengths reflected from the blood. This probe is simply attached to your finger, earlobe, or another place on the body. [1]¬ Oxygen saturation values of 95% to 100% are generally considered normal. Values under 90% could quickly lead to a serious deterioration in status, and values under 70% are life-threatening.[3] In this project, we took SpO2 = 90% as a standard. If the oxygen saturation is less than 90%, we assume that he/she may be infected with COVID-19.

#### Heart Rate
Your heart rate, or pulse, is the number of times your heart beats in 1 minute. Heart rates vary from person to person. It’s lower when you’re at rest and higher when you exercise.[4] Usually, it can be affected by multiple factors such as weather, emotions, body size, diseases, medications, caffeine and nicotine, etc. “We’re seeing a lot of patients with symptoms of palpitations or an increase in heart rate with minimal activity, where prior to COVID, they weren’t having any of these symptoms,” says Riple Hansalia, M.D., a cardiac electrophysiologist at Jersey Shore University Medical Center. “That’s been pretty common in our practice, nationally and worldwide.”[5] Therefore, we can use heart rate as a supplement health index to detect COVID-19.

A normal resting heart rate is usually between 60 and 100 beats per minute (bpm). Your number may vary. Children tend to have higher resting heart rates than adults.[4] In this project, if the heart rate measured is continuously higher than 100 bpm, together with the abnormal oxygen saturation, we will inform the user that he/she is at risk of COVID-19 and had better take a COVID-19 test; if the heart rate is too low, for example lower than 60 bpm, the user will be informed of the danger of disease, but not COVID-19.

### Sensor(s) Used
The only one sensor used in this project is MAX30102 heart rate sensor, which can be used to measure both oxygen saturation and heart rate.

#### MAX30102

<p align="center">
    <img src="https://github.com/Mr-Msz/HomemadeHealthMonitorCovid/blob/main/Figure/1_1.jpg"/>
</p>
<p align="center">Figure 1 MAX30102 heart rate sensor</p>

● Heart-Rate Monitor and Pulse Oximeter Sensor in LED Reflective Solution 

● Tiny 5.6mm x 3.3mm x 1.55mm 14-Pin Optical Module • Integrated Cover Glass for Optimal, Robust Performance 

● Ultra-Low Power Operation for Mobile Devices 

    •	Programmable Sample Rate and LED Current for Power Savings 

    •	Low-Power Heart-Rate Monitor (< 1mW) 

    •	Ultra-Low Shutdown Current (0.7μA, typ) 

● Fast Data Output Capability 

    •	High Sample Rates 

● Robust Motion Artifact Resilience • High SNR 

● -40°C to +85°C Operating Temperature Range 

<p align="center">
    <img src="https://github.com/Mr-Msz/HomemadeHealthMonitorCovid/blob/main/Figure/1_2.png"/>
</p>
<p align="center">Figure 2 System diagram of MAX30102[6]</p>

Figure 2 is the system diagram of MAX30102, which shows that the chip can be divided into two parts. One is the analog signal acquisition circuit, which emits light of a specific wavelength through RED and IR lamps to collect the light reflected back from the human body. The optical signal is converted into electrical signal through PD tube, and finally converted into digital signal through 18-bit ADC converter.
The second part is the digital processing circuit, which filters the original data converted by ADC and places it in the buffer. The MCU reads and writes the internal registers of the chip through the IIC interface and reads and takes out the corresponding data.

The MAX30102 module applies to photoelectric volume method to measure heart rate and oxygen saturation. The basic principle of photoelectric volume method is to measure pulse and oxygen saturation by using the different light transmission rate caused by human tissues when blood vessels pulsate. The sensor, which consists of a light source and an optical converter, are attached to the patient's finger, wrist or earlobe with straps or clips. The light source is usually led with specific wavelength (red light near 660nm and infrared light near 900nm), which is selective for oxygenated hemoglobin (HbO2) and deoxygenated hemoglobin (Hb) in arterial blood. When the light beam passes through the peripheral blood of the human body, the transmittance of the light changes due to the change of the volume of arterial pulsation congestion. At this time, the photoelectric converter receives the light reflected by the human body tissue, converts it into electrical signal, and amplifies and outputs it. As the pulse is a signal that changes periodically with the beating of the heart, and the volume of the arterial vessels also changes periodically, the change period of the electrical signal of the photoelectric converter is the pulse rate. Meanwhile, according to the definition of blood oxygen saturation, it can be expressed as:

<p align="center">
    <img src="https://github.com/Mr-Msz/HomemadeHealthMonitorCovid/blob/main/Figure/formula.png"/>
</p>

<p align="center">
    <img src="https://github.com/Mr-Msz/HomemadeHealthMonitorCovid/blob/main/Figure/1_3.jpg"/>
</p>
<p align="center">Figure 3 Absorption of oxygenated hemoglobin (HbO2) and deoxygenated hemoglobin (Hb) at different wavelengths[7]</p>

The MAX30102 consists of a complete LED and drive part, light sensing and AD conversion part, ambient light interference elimination and digital filtering part, leaving only the digital interface to the user, greatly reducing the user's design burden. The user only needs to read THE FIFO of MAX30102 through hardware I2C or analog I2C interface with the MCU, and then the converted light intensity value can be obtained. The heart rate value and blood oxygen saturation can be obtained by writing the corresponding algorithm.

### Signal Conditioning and Processing

## Experiments and Results
### Code
```markdown
#### Coding Part
```

## Discussion

## References
[1] Deborah Leader, R. N. (2021, July 22). The importance of O2 sats with COPD. Verywell Health. Retrieved October 5, 2021, from https://www.verywellhealth.com/oxygen-saturation-914796. 

[2] What you need to know about your blood oxygen level. Banner. (n.d.). Retrieved October 5, 2021, from https://www.bannerhealth.com/healthcareblog/teach-me/blood-oxygen-level-what-you-need-to-know. 

[3] Cameron, M. H., & Monroe, L. G. (2007). Chapter 22 - Vital Signs. In Physical rehabilitation: Evidence-based examination, evaluation, and intervention. essay, Saunders/Elsevier. 

[4] Beckerman, J. (2021, August 18). Heart rate: Normal pulse, Measurement, Max and target heart rate . WebMD. Retrieved October 5, 2021, from https://www.webmd.com/heart-disease/heart-failure/watching-rate-monitor. 

[5] Hansalia, R. (2021, August 18). Does covid-19 cause heart rate issues? Hackensack Meridian Health. Retrieved October 5, 2021, from https://www.hackensackmeridianhealth.org/HealthU/2021/08/18/does-covid-19-cause-heart-rate-issues/. 

[6] MAX30102 high-sensitivity pulse oximeter and heart-rate. (n.d.). Retrieved October 5, 2021, from https://www.maximintegrated.com/en/products/interface/sensor-interface/MAX30102.html. 

[7] MAX30102 initial use and heart rate, blood oxygen measurement principle. Retrieved October 5, 2021, from http://home.eeworld.com.cn/my/space-uid-363835-blogid-589641.html

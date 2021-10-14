## Current Progress - 10/02/2021

### Update
Instead of making a sensor ourselves and try to compare with the state-of-art, we decide to be more realistic on our goals. Still, we will use MAX30102 as our main sensor. At the same time, we will try to put it together with Raspberry Pi which is not its originally intended platform. If time is enough, we will try to compare its characteristics with some oximeter on market. For the self-reported part of the device, after reading some related materials, we decide to change it to a device that is visualizable and can be used as a self-check measure for users. This will require a 16x2 LCD to perform.

We received our MAX30102 and began to work on the hardware part of the project. We prepare to work on the paper simultaneously in case we encounter some difficult situation later.

### Problems Encountered
As MAX30102 is not originally produced for Raspberry Pi, we encountered with a problem of how to light the sensor up. Because of its compatibility, the official code seems to be not working. We will need a package for MAX30102 for Raspberry Pi.

### Future Plan

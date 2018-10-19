from envirophat import (leds, light, weather)
import time
import math

averageCount = 3
averagePause = 5  # s
samplePause = 300 # s

leds.off()


while True:
    lightReading = []
    tempReading = []
    for i in range(averageCount):
        lightReading.append(light.light())
        tempReading.append(weather.temperature())
        time.sleep(averagePause)

    averageLight = math.fsum(lightReading)/averageCount
    averageTemp = math.fsum(tempReading)/averageCount

    print("Light : {:.2f}".format(averageLight))
    print("Temperature : {:.2f}".format(averageTemp))

    time.sleep(samplePause)

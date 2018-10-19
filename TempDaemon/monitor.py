from envirophat import (leds, light, weather)
import time
import math

averageCount = 3
averagePause = 5  # s

leds.ofF()


while True:
    lightReading = []
    tempReading = []
    for i in range(averageCount):
        lightReading[i] = light.light()
        tempReading[i] = weather.temperature()
        time.sleep(averagePause)

    averageLight = math.fsum(lightReading)/averageCount
    averageTemp = math.fsum(tempReading)/averageCount

    print("Light : {:.2f}".format(averageLight))
    print("Temperature : {:.2f}".format(averageTemp))

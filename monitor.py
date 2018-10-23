from envirophat import (leds, light, weather)
import time
import math
import requests
from datetime import datetime

url = "https://temp-scanner.azurewebsites.net/api/reading"


averageCount = 3
averagePause = 5  # s
samplePause = 300 # s

leds.off()


while True:
    lightReading = []
    tempReading = []
    pressure = []
    timeReadings = []

    for i in range(averageCount):
        lightReading.append(light.light())
        tempReading.append(weather.temperature())
        pressure.append(weather.pressure())
        timeReadings.append(int(datetime.utcnow()))

        time.sleep(averagePause)

    averageLight = math.fsum(lightReading)/averageCount
    averageTemp = math.fsum(tempReading)/averageCount
    averagePressure = math.fsum(pressure)/averageCount
    averageTime = math.fsum(timeReadings)/averageCount

    print("Light : {:.2f}".format(averageLight))
    print("Temperature : {:.2f}".format(averageTemp))
    print("Pressure : {:.2f}").format(averagePressure))
    print("Time : {:.2f}").format(averageTime))

    time.sleep(samplePause)

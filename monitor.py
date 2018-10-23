from envirophat import (leds, light, weather)
import time
import math
import requests
from datetime import datetime

url = "https://temp-scanner.azurewebsites.net/api/reading"


averageCount = 3
averagePause = 5  # s
samplePause = 300  # s

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
        d = datetime.utcnow()
        timeReadings.append(int(datetime.utcnow().timestamp()))

        time.sleep(averagePause)

    averageLight = math.fsum(lightReading)/averageCount
    averageTemp = math.fsum(tempReading)/averageCount
    averagePressure = math.fsum(pressure)/averageCount
    averageTime = math.fsum(timeReadings)/averageCount

    obj = {"LightLevel": averageLight, "Temperature": averageTemp, "Pressure": averagePressure, "Time": averageTime }

    print(obj)

    time.sleep(samplePause)

# temp sensor simulator
# John Taylor
# UC Boulder
# 01.19.2021

import random
import datetime
import time
import json
import os.path
from os import path


class TempSensor:
    alarmThreshold = 5
    sleepTime = 1  # seconds

    def __init__(self, number, nominalTemp):
        self.number = number
        self.nominalTemp = nominalTemp
        self.alarmCount = 0
        self.errorCount = 0

    def readSensor(self):
        # calculate a random number to simulate probabilities
        probability = random.random()
        # generate a number between -2 and 2 and add to nominal temp
        sensorReading = self.nominalTemp + (random.random() * 4 - 2)

        # 80 percent of the time
        if 0.8 > probability >= 0:
            # sensor will read nominal +- 2 degrees
            return sensorReading
        # 10 percent of the time
        elif 0.9 > probability >= 0.8:
            # sensor will read nominal +- 2 degrees with an additional +- 8 degrees
            if sensorReading < self.nominalTemp:
                sensorReading -= 8
            else:
                sensorReading += 8
            return sensorReading
        # 10 percent of the time
        elif 1 > probability >= 0.9:
            # sensor will return NA
            return "N/A"

    def updateFile(self, data):
        # check if file already exisits
        if not path.exists(str(self.number) + ".txt"):
            print("File doesn't exist, creating it now")
            newFile = open(str(self.number) + ".txt", 'a+')
            initialData = {"samples": []}
            json.dump(initialData, newFile, indent=4)
            newFile.close()
        json_file = open(str(self.number) + ".txt", 'r+')
        try:
            file_data = json.load(json_file)
        except ValueError as error:
            print(error)
            print("File Is Empty, Writing initial Data")
            json_file.seek(0)
            json.dump(data, json_file, indent=4)
            json_file.close()
        else:
            # append data to the end of the file
            file_data["samples"].append(data)
            json_file.seek(0)
            json.dump(file_data, json_file, indent=4)
            json_file.close()

    def begin(self):
        while True:
            reading = self.readSensor()
            if reading == "N/A":
                self.errorCount += 1
            elif reading > self.nominalTemp + self.alarmThreshold or reading < self.nominalTemp - self.alarmThreshold:
                self.alarmCount += 1
            data = {"Sensor Number": self.number,
                    "timestamp": str(datetime.datetime.now()),
                    "temp": str(reading),
                    "alarm count": self.alarmCount,
                    "error count": self.errorCount
                    }
            self.updateFile(data)
            time.sleep(self.sleepTime)

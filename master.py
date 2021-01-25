# master system
# John Taylor
# UC Boulder
# 01.21.2021

import json
import glob
import time
from tabulate import tabulate


class Master:
    sleepTime = 30  # seconds

    def __init__(self):
        self.errorCount = 0

    def begin(self):
        while True:
            time.sleep(self.sleepTime)
            # grab all the text files in the directory
            textFiles = glob.glob('*.txt')
            tableData = []
            for fileName in textFiles:
                try:
                    with open(fileName) as f:
                        data = json.load(f)
                        # get the last 10 items in the list
                        lastTenSamples = data["samples"][-10:]
                        hi = self.getHighTemp(lastTenSamples)
                        lo = self.getLowTemp(lastTenSamples)
                        avg = self.getAvg(lastTenSamples)
                        errorCount = lastTenSamples[-1]["error count"]
                        alarmCount = lastTenSamples[-1]["alarm count"]
                        sensorNumber = lastTenSamples[-1]["Sensor Number"]
                        tableData.append(
                            [str(sensorNumber), str(lo), str(avg), str(hi), str(errorCount), str(alarmCount)])
                except OSError:
                    print("Could not open/read file:", fileName)
                    errorCount += 1;
                    print("ErrorCount: " + errorCount)
            print(tabulate(tableData, headers=["System", "Low", "Avg", "High", "Error Count", "Alarm Count"]))

    # function to return the highest
    # temperature in the dataset passed to it
    def getHighTemp(self, data):
        high = None
        for sample in data:
            try:
                tempF = float(sample['temp'])
                if high is None:
                    high = tempF
                elif tempF > float(high):
                    high = tempF
            except ValueError:
                self.errorCount += 1
        return str(high)

    # function to return the lowest
    # temperature in the dataset passed to it
    def getLowTemp(self, data):
        low = None
        for sample in data:
            try:
                tempF = float(sample['temp'])
                if low is None:
                    low = tempF
                elif tempF < float(low):
                    low = tempF
            except ValueError:
                self.errorCount += 1
        return str(low)

    # function to return the average
    # temperature in the dataset ignoring N/A data
    def getAvg(self, data):
        # sum of the average
        total = 0
        # number to average over
        count = 0
        for sample in data:
            try:
                tempF = float(sample['temp'])
                total += tempF
                count += 1
            except ValueError:
                self.errorCount += 1
        if count > 0:
            # prevent divide by 0 in the case of no data
            average = total / count
            return str(average)

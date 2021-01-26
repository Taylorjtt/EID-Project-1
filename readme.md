_John Taylor_
# Simulated Temperature Sensor/Monitoring System
## Introduction
This repository includes software that simulates temperature sensors using python. This software was tested on ubuntu 18.0.4 LTS. It was written with Python 3.6.9. In order to run the code you must install the tabulate library

	sudo apt-get install -y python3-tabulate

once tabulate is installed you may run the project with the following command
		
		python3 main.py
## Design
### Assumptions
I assumed that the sign of the +/- 8 deg F spike would be the same as the +/- 2 degree noise of the sample. For example if the sample had initial noise of -0.5 degrees and the spike event occoured -8 degrees would be added to the measured temperature
### Temperature sensor
The temperature sensor portion of the project is a python class that simulates a  temperature sensor that is effected by noise and sometimes fails to communicate. 
- 80% of the time the temp sensor outputs it's (nominal temp) +/- (2 degrees F)
- 10% of the time the temp sensor outputs  a spike of  (nominal temp) +/- (2 degrees F) +/- (8  degrees F)
- 10% of the time the temp sensor outputs N/A

An alarm occurs and alarm count is incremented if the sensor output is out of the range of +/- 5 degrees F
An error occurs and error count is incremented  if the sensor output is N/A

In order to generate the events based on probability I generate a random number from 0-1. 
- if that number is < 0.8 the 80% probability event happens
- if 0.8 < number < 0.9 the first 10% probability event occurs
- if 0.9 < number < 1 the second 10% probability event occurs

Once the begin method is called, the temp sensor will take a sample every 10s and append that sample in JSON format to a file in the program directory.

### Master Program
The master program looks for  text files in the program directory to read. Every 30 seconds it reads the text files and provides statistics on the last 10 samples as well as error counts and alarm counts. If the master has an alarm, the master alarm count is incremented and displayed

### Main Program
The main program creates separate processes to run 3 temperature sensors and the master program.



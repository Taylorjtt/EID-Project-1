from TempSensor import TempSensor
from master import Master
from multiprocessing import Process

# https://stackoverflow.com/questions/18204782/runtimeerror-on-windows-trying-python-multiprocessing
if __name__ == '__main__':
    # create 3 temp sensors
    t1 = TempSensor(1, 70);
    t2 = TempSensor(2, 70);
    t3 = TempSensor(3, 70);

    # create the master
    master = Master()

    # Create seperate processes to run the sensor/master begin methods
    # https://stackoverflow.com/questions/26239695/parallel-execution-of-class-methods
    process1 = Process(target=t1.begin)
    process2 = Process(target=t2.begin)
    process3 = Process(target=t3.begin)
    masterProcess = Process(target=master.begin);

    # start those processes
    process1.start();
    process2.start();
    process3.start();
    masterProcess.start();

    # call join so the program knows to wait for these processes
    # to complete before exiting
    process1.join();
    process2.join();
    process3.join();
    masterProcess.join();



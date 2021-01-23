from TempSensor import TempSensor
from master import Master
from multiprocessing import Process

# https://stackoverflow.com/questions/18204782/runtimeerror-on-windows-trying-python-multiprocessing
if __name__ == '__main__':
    t1 = TempSensor(1, 70);
    t2 = TempSensor(2, 70);
    t3 = TempSensor(3, 70);
    master = Master()

    # https://stackoverflow.com/questions/26239695/parallel-execution-of-class-methods
    process1 = Process(target=t1.begin)
    process2 = Process(target=t2.begin)
    process3 = Process(target=t3.begin)
    masterProcess = Process(target=master.begin);

    process1.start();
    print("here")
    process2.start();
    process3.start();
    masterProcess.start();

    process1.join();
    process2.join();
    process3.join();
    masterProcess.join();



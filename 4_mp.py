#-------------------------------------------------------------------------------------------
# Alem Fitwi: Multiprocessing; it strictly needs to be run within main method
#-------------------------------------------------------------------------------------------
# Standard Modules
#-------------------------------
import time
import multiprocessing as mp
from time import perf_counter

#-------------------------------------------------------------------------------------------
# Global Variables
#-------------------------------
tmp_dct = {'x': 2, 'y':3}

#-------------------------------------------------------------------------------------------
# Sample Functions
#-------------------------------
#--- Main Thread
def func1(queue):
    x = tmp_dct['x']
    tmp_dct['y'] = 7
    t1 = perf_counter()
    sum = 0
    for i in range(x**20):
        sum+=i
    t2 = perf_counter()
    tmp_dct['time1'] = t2-t1
    queue.put(tmp_dct)

def func2(queue):
    x = tmp_dct['x']
    t1 = perf_counter()
    sum = 0
    for i in range(x**20):
        sum+=i
    t2 = perf_counter()
    tmp_dct['time2'] = t2-t1
    queue.put(tmp_dct)

#-------------------------------------------------------------------------------------------
# Without Multiprocessing
#-------------------------------
#print(f"func1: {func1(2)}")
#print(f"func2: {func2(2)}")

#-------------------------------------------------------------------------------------------
# Implementation of multiprocessing
#-------------------------------
def get_mpresults():
    queue = mp.Queue()
    queue.put(tmp_dct)
    bar = mp.Process(target=func1, args=(queue,))
    mouse = mp.Process(target=func2, args=(queue,))
    bar.start()
    mouse.start()
    bar.join()
    mouse.join()
    return queue.get()

#-------------------------------------------------------------------------------------------
# '__main__': Mandatory with multiprocessing in Windows OS
#-------------------------------
if __name__ == '_main__':
    result = get_mpresults()
    print(f"r1: {result['time1']}")
    print(f"r1: {result['time1']}")

#-------------------------------------------------------------------------------------------
#                                 ~END~
#-------------------------------------------------------------------------------------------
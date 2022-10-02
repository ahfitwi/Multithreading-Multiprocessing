#-------------------------------------------------------------------------------------------
# Alem Fitwi: Multihreading
#-------------------------------------------------------------------------------------------
# Standard Modules
#-------------------------------
import time
from time import perf_counter
from concurrent.futures import ThreadPoolExecutor as tpe

#-------------------------------------------------------------------------------------------
# Sample Functions
#-------------------------------
#--- Main Thread
def func1(x):
    time.sleep(2)
    for i in range(x):
        print('f1', end='\t')
    return x+2

def func2(x):
    time.sleep(2)
    for i in range(x):
        print('f2', end='\t')
    return x+3


#-------------------------------------------------------------------------------------------
# Context Manager: returns type of a future from the pool of threads
#-------------------------------
with tpe(max_workers=2) as e: #a max of 2 threads are created
    future1 = e.submit(func1, 3)
    future2 = e.submit(func2, 3)

#-------------------------------------------------------------------------------------------
# Get Results: concurrently but not in parallel
#-------------------------------
print(f"\n Returned value from func1: {future1.result()}")
print(f"\n Returned value from func2: {future2.result()}")

"""f1      f1      f1      f2      f2      f2
 Returned value from func1: 5

 Returned value from func2: 6
 """
#-------------------------------------------------------------------------------------------
#                                 ~END~
#-------------------------------------------------------------------------------------------

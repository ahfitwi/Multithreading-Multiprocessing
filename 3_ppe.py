#-------------------------------------------------------------------------------------------
# Alem Fitwi: Multiprocessing
#-------------------------------------------------------------------------------------------
# Standard Modules
#-------------------------------
import time
from time import perf_counter
from concurrent.futures import ProcessPoolExecutor as ppe

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
# **************************************************************************
# Run the ppe within a main function: if __name__ == '__main__":
#***************************************************************************
if __name__ == "__main__":
    with ppe(max_workers=2) as e: #a max of 2 threads are created
        future1 = e.submit(func1, 3)
        future2 = e.submit(func2, 3)

#-------------------------------------------------------------------------------------------
# Get Results: concurrently but not in parallel
#-------------------------------
# Broken Process Pool
#-------------------------------------------------------------------------------------------
#                                 ~END~
#-------------------------------------------------------------------------------------------

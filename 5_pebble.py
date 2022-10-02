#-------------------------------------------------------------------------------------------
# Alem Fitwi: @concurrent.process 
#-------------------------------------------------------------------------------------------
# Standard Modules
#-------------------------------
import time
import multiprocessing as mp
from time import perf_counter

from pebble import concurrent

#-------------------------------------------------------------------------------------------
# Decorate Function
#-------------------------------
@concurrent.process
def function(args):
    print("Here ------------")
    x,y,z = args
    t1 = perf_counter()
    sum = 0
    for i in range(x**20):
        sum+=i
    t2 = perf_counter()
    return t2-t1
#-------------------------------------------------------------------------------------------
# '__main__': Mandatory with multiprocessing in Windows OS
#-------------------------------
if __name__ == '_main__':
    future = function([2, 5,3], [3, 4, 5])
    print(future.result())

#-------------------------------------------------------------------------------------------
#                                 ~END~
#-------------------------------------------------------------------------------------------

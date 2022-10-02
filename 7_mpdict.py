#-------------------------------------------------------------------------------------------
# Alem Fitwi: multiprocessing.Pool
#-------------------------------------------------------------------------------------------
# Standard Modules
#-------------------------------
import time
from multiprocessing import Process, Array, Manager, Value, Lock
from time import perf_counter

#-------------------------------------------------------------------------------------------
# Sample Function
#-------------------------------
def func1(dct):
    time.sleep(2)
    dct['key'] +=999
    dct['uni'] = False 
  
#-------------------------------------------------------------------------------------------
# Implement The Multiprocessing
#-------------------------------
def main(dct1):
    manager = Manager()
    dct =  manager.dict()
    dct.update(dct1)
    #---------------------------------------------------------------------------------------
    # Start The Two Threads
    #-------------------------------
    p1 = Process(target=func1, args = (dct,)) # (dct,): tuple, never forget comman for 1 arg
    p2 = Process(target=func1, args = (dct,)) # (dct,): tuple, never forget comman for 1 arg

    #---------------------------------------------------------------------------------------
    # Start The Two Processes
    #-------------------------------
    p1.start()
    p2.start()

    #---------------------------------------------------------------------------------------
    # Join The Two Processes (Hold Until Completion of Task)
    #-------------------------------
    p1.join()
    p2.join()

    return dct


#-------------------------------------------------------------------------------------------
# '__main__': Mandatory with multiprocessing in Windows OS
#-------------------------------
if __name__ == "__main__":
    tt1 = perf_counter()
    
    dct1 = {}
    dct1['key'] = 1
    dct1['uni'] = False
    """
    func1(dct)
    func1(dct)
    print(f"SeqTime = {perf_counter()-tt1}")
    
    manager = Manager()
    dct =  manager.dict()
    dct['key'] = 1
    dct['uni'] = False
    
    #---------------------------------------------------------------------------------------
    # Start The Two Threads
    #-------------------------------
    p1 = Process(target=func1, args = (dct,)) # (dct,): tuple, never forget comman for 1 arg
    p2 = Process(target=func1, args = (dct,)) # (dct,): tuple, never forget comman for 1 arg

    #---------------------------------------------------------------------------------------
    # Start The Two Processes
    #-------------------------------
    p1.start()
    p2.start()

    #---------------------------------------------------------------------------------------
    # Join The Two Processes (Hold Until Completion of Task)
    #-------------------------------
    p1.join()
    p2.join()
    """
    dct = main(dct1)
    print(f"dct: {dct}")
    print(f"SeqTime = {perf_counter()-tt1}")
#-------------------------------------------------------------------------------------------
#                                 ~END~
#-------------------------------------------------------------------------------------------
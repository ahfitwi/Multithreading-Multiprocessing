#-------------------------------------------------------------------------------------------
# Alem Fitwi: Threading
#-------------------------------------------------------------------------------------------
# Standard Modules
#-------------------------------
import time
import threading as th #Sequential, GIL not unlocked
from time import perf_counter

#-------------------------------------------------------------------------------------------
# Sample Functions
#-------------------------------
#--- Main Thread
def func1(x):
    time.sleep(1)
    for i in range(x):
        print('f1', end='\t')

def func2(x):
    time.sleep(2)
    for i in range(x):
        print('f2', end='\t')

print("\n Executing from main thread!.")

#-------------------------------------------------------------------------------------------
# Create Two Threads
#-------------------------------
t1 = th.Thread(target=func1, args=(3,))
t2 = th.Thread(target=func2, args=(3,))

#-------------------------------------------------------------------------------------------
# Start The Two Threads
#-------------------------------
t1.start()
t2.start()

#-------------------------------------------------------------------------------------------
# Join Threads, Waits until Tasks are completed
#-------------------------------
t1.join()
t2.join()

#-------------------------------------------------------------------------------------------
# Back To Main Thread
#-------------------------------

print("Back to Main Thread!")

#-------------------------------------------------------------------------------------------
# Results: with or without t1/t2.join() but with no sleep time.
#-------------------------------
"""Executing from main thread!.
f1      f1      f1     f2      f2      f2      Back to Main Thread"""

#-------------------------------------------------------------------------------------------
# Results: without t1/t2.join() but with sleep.time(2) in func2
#-------------------------------
"""Executing from main thread!.
f1      f1      f1   Back to Main Thread!    f2      f2      f2"""

#-------------------------------------------------------------------------------------------
# Results: without t1/t2.join() but with sleep.time(2) in func2 and time.sleep(1) in func1
#-------------------------------
"""Executing from main thread!.
Back to Main Thread!
f1      f2      f2      f2      f1      f1"""

#-------------------------------------------------------------------------------------------
# Results: witht1/t2.join() and with sleep.time(2) in func2
#-------------------------------
"""Executing from main thread!.
f1      f2      f2      f2      f1      f1      Back to Main Thread!"""

#-------------------------------------------------------------------------------------------
#                                 ~END~
#-------------------------------------------------------------------------------------------
# example of multi threading
# Running two thread parallally
from threading import * #importing forthread
from time import *
class Hello(Thread): # inheriting Thread class
    def run(self): # overriding built in mathod of thread class
        for i in range(10):

            print("Hello")
            sleep(1) # for delay
class Hi(Thread):
    def run(self):
        for i in range(10):
            print("Hi")
            sleep(1)

t1=Hello()
t2=Hi()

t1.start() # calling run method parallal
sleep(0.2)
t2.start()
t1.join()
t2.join()
print("Bye") # for displaying bye at last you have to execute join
# threading by creating a messenger thats bro's messenger

import threading

class BrosMessenger(threading.Thread):
    def run(self):
        for _ in range(10): #dont care about the variable just put a dash/underscore _ as replacement
            print(threading.currentThread().getName()) # we want to do 10 times is to name the threads like 2 diffr threads w/ two diffr names running at a same exact time

x = BrosMessenger(name='Send messages')
y = BrosMessenger(name='Receive messages')
x.start()
y.start()
# when u call start the prog goes to class and say run at the same time for both sending and receiving with no counter

# try running the prog
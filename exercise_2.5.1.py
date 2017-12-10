'''
Zaimplementowac prosty problem pieciu filozofów (z deadlockiem), nastepnie usunac deadlock.
'''
import time
import threading

# Script without deadlock


def eating(nr, forks):
    print("Start")

    if ((nr + 1) % 5 > nr):
        forks[nr % 5].acquire()
        time.sleep(5)
        forks[(nr + 1) % 5].acquire()
    else:
        forks[(nr + 1) % 5].acquire()
        time.sleep(5)
        forks[nr % 5].acquire()

    print("Eat")

    if ((nr + 1) % 5 > nr):
        forks[(nr + 1) % 5].release()
        forks[nr % 5].release()
    else:
        forks[nr % 5].release()
        forks[(nr + 1) % 5].release()

    print("End")

class myThread(threading.Thread):
    def __init__(self, nr, forks):
        threading.Thread.__init__(self)
        self.forks = forks
        self.nr = nr
        self.lock = lock

    def run(self):
        eating(self.nr, self.forks)

forks = []
for i in range(0, 5):
    forks.append(threading.Lock())
lock = threading.Lock()
threads = []


try:
    thread0 = myThread(0, forks).start()
    thread1 = myThread(1, forks).start()
    thread2 = myThread(2, forks).start()
    thread3 = myThread(3, forks).start()
    thread4 = myThread(4, forks).start()

except:
    print("Error: unable to start thread")

print("The end")
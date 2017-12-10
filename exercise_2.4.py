'''
Zaimplementowac wielowatkowe liczenie histogramu (monitorowac wykonanie htop).
'''

from matplotlib import pyplot as plt
import queue
import threading
import math
import numpy as np


def createList(size):
    data = np.random.normal(0, 500, size)
    return data


def createHistogram():
    data = createList(10000)
    bins = np.linspace(math.ceil(min(data)), math.floor(max(data)), 20)
    data1 = {'data': data, 'bins': bins}
    return data1


queue = queue.Queue()
class threadHistogram(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        data = createHistogram()
        queue.put(data)


threadHistogram().start()
threadHistogram().start()
threadHistogram().start()

data1 = queue.get()
data2 = queue.get()
data3 = queue.get()

plt.figure(1)
plt.xlim([min(data1['data'])-5, max(data1['data'])+5])
plt.subplot(311)
plt.hist(data1['data'], data1['bins'], alpha=0.5)
plt.subplot(312)
plt.hist(data2['data'], data2['bins'], alpha=0.5)
plt.subplot(313)
plt.hist(data3['data'], data3['bins'], alpha=0.5)
plt.show()













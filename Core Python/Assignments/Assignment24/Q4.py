from threading import Thread, Lock
import time
import random

lock = Lock()
item = 0
signal = 0

def producer(name):
    global item, signal
    for i in range(5):
        lock.acquire()
        if signal == 0:
            item = random.randint(1, 100)
            print(name, "produced item:", item)
            signal = 1
        lock.release()
        time.sleep(random.uniform(0.5, 1.5))

def consumer(name):
    global item, signal
    for i in range(5):
        lock.acquire()
        if signal == 1:
            print(name, "consumed item:", item)
            signal = 0
        lock.release()
        time.sleep(random.uniform(0.5, 1.5))

if __name__ == "__main__":
    p1 = Thread(target=producer, args=("Producer-1",))
    p2 = Thread(target=producer, args=("Producer-2",))
    c1 = Thread(target=consumer, args=("Consumer-1",))
    c2 = Thread(target=consumer, args=("Consumer-2",))

    p1.start()
    p2.start()
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    c1.join()
    c2.join()

    print("\nAll threads completed successfully.")

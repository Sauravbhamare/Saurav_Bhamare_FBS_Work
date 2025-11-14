from threading import Thread , Lock
import time

lock = Lock()

def cal_lowercase():
    for ch in "abcdefghijklmnopqrstuvwxyz":
        lock.acquire()
        print("Lowercase:", ch)
        lock.release()
        time.sleep(0.1)
        
def cal_uppercase():
    for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        lock.acquire()
        print("Uppercase:",ch)
        lock.release()
        time.sleep(0.1)
        
if(__name__ == '__main__'):
    t1 = Thread(target=cal_lowercase)
    t2 = Thread(target=cal_uppercase)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("\nAll Threads completed successfully.")
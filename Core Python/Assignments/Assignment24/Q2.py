from threading import Thread , Lock
import time
lock = Lock()
num = 1
limit = 10

def cal_odd():
    global num
    while(num <= limit):
        lock.acquire()
        if(num % 2 != 0):
            print("Odd:",num)
            num += 1
        lock.release()
        time.sleep(0.1)
        
def cal_even():
    global num
    while(num <= limit):
        lock.acquire()
        if(num % 2 == 0):
            print("Even:",num)
            num += 1
            lock.release()
            time.sleep(0.1)
            
if(__name__ == '__main__'):
    t1 = Thread(target=cal_odd)
    t2 = Thread(target=cal_even)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("\nAll threads completed Successfully.")
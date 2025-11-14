from threading import Thread, Lock

total_sum = 0
lock = Lock()

def calc_sum(start, end, thread_name):
    global total_sum
    local_sum = 0
    
    for i in range(start, end+1):
        local_sum += i*i
        
    lock.acquire()
    print(thread_name,"Range","-",end,"Partial Sum=",local_sum)
    total_sum += local_sum
    lock.release()
    
    
if(__name__ == '__main__'):
    t1 = Thread(name='Thread1', target=calc_sum, args=(1, 25, 'Thread1'))
    t2 = Thread(name='Thread2', target=calc_sum, args=(26, 50, 'Thread2'))
    t3 = Thread(name='Thread3', target=calc_sum, args=(51, 75, 'Thread3'))
    t4 = Thread(name='Thread4', target=calc_sum, args=(76, 100, 'Thread4'))
    
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    
    print("\nAllthreads completed Successfully")
    print(f"Total Sum of Squares from 1 to 100 = {total_sum}")

    
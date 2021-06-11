"""
import time
def bak():
    print("bak calisti")
    c=2
    d=1
    counter(c,d)
def calis(c,d):
    print("calis",c,d)
    a=input("sayi gir")
    return a
def counter(c,d): 
    t=0
    calis=calis(c,d)
    while t<10: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t += 1
        if calis==2:
            break
        if t==5:
            print("aaa")
            break
      
    print('Fire in the hole!!')
    
bak()
"""
import threading
import Queue

def stringFunction(value, out_queue):
    my_str = "This is string no. " + value
    out_queue.put(my_str)

my_queue = Queue.Queue()
thread1 = threading.Thread(stringFunction("one", my_queue))
thread1.start()
thread1.join()

func_value = my_queue.get()
print (func_value)
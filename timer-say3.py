import time
import threading

time_say_okutuldu=0
online_okutuldu=1
irs_role_tetik=0

def counter():
    global time_say_okutuldu
    global online_okutuldu
    global irs_role_tetik
    t=0
    if time_say_okutuldu==0:
        if online_okutuldu==1 :
            while t<5:
                print("t:",t)
                if irs_role_tetik==1 :
                    print("break")
                    break                   
                else:
                    time.sleep(1) 
                    t += 1
                    print(t)
            if t==5:
                time_say_okutuldu=1
            t=0
            print("#########",t,"##########")
def func():
    global irs_role_tetik
    time.sleep(3)
    irs_role_tetik=1
    print("irs_role_tetik",irs_role_tetik)
  
if __name__ == "__main__":
    while True:
        t1=threading.Thread(target=counter)
        t2=threading.Thread(target=func)
        t1.start()
        t2.start()
        t1.join()
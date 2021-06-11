import time
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
                if t==2:
                    irs_role_tetik=1
                    
                if irs_role_tetik==1 :
                    print("break")
                    break                   
                else:
                    time.sleep(1) 
                    t += 1
                    print(t)
            if t==5:
                time_say_okutuldu=1
                print("time_say_okutuldu",time_say_okutuldu)
                
            t=0
            irs_role_tetik=0
            print("#########",t,"##########")

counter()

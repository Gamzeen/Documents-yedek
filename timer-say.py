import time
irs_role_tetik=1
a=1
def counter():
    global a
    global irs_role_tetik
    t=0
    while t<5:
        print("while t:",t)
        if irs_role_tetik==1 :
            a=1
            print("break a")
            break
        else:
            irs_role_tetik=1
            time.sleep(1) 
            t += 1
            print(t)
        
    print("while sonrasi t",t)
    t=0
    print("t sınrasi t--",t)
    
counter()
counter()
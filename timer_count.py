import time 
time_out=0 
# define the countdown func. 
def counter(): 
    global time_out
    t=0
    while t<5: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t += 1
        if t==5:
            print("aaa")
            time_out=t
         
      
    print('Fire in the hole!!')
    return t
a=counter() 
print(a)
print(time_out)
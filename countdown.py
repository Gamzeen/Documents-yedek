import time 
  
# define the countdown func. 
def countdown(t): 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
        if t==0:
            print("aaa")
      
    print('Fire in the hole!!') 
  
  
# input time in seconds 
#t = input("Enter the time in seconds: ") 
  
# function call 
countdown(int(5)) 
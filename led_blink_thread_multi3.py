import RPi.GPIO as GPIO
import time
import threading
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
# blinking function
GPIO.setup(37, GPIO.OUT) #pin numarasina gore
GPIO.setup(38, GPIO.OUT) #pin numarasina gore
GPIO.setup(40, GPIO.OUT)
a=0
b=0
global i
def func():
    global a
    global b
    while True:
        time.sleep(3)
        a=1
        b=1

def led_setup():
    GPIO.output(37,GPIO.LOW)
    GPIO.output(38,GPIO.LOW)
    GPIO.output(40,GPIO.LOW)
def blink_high(pin):
    GPIO.output(pin,GPIO.HIGH)
def blink_low(pin):
    GPIO.output(pin,GPIO.LOW)

def led_blink():
    if a==1:
        print("blink(37)",blink_high(37))
        time.sleep(2)
        print("blink(37)",blink_low(37))
    
    if b==1:
        print("blink(40)",blink_high(40))
        time.sleep(2)
        print("blink(40)",blink_low(40))
def led_blink2(): 
    print("blink(38)",blink_high(38))
    time.sleep(2)
    print("blink(38)",blink_low(38))
         
if __name__ == "__main__":
    led_setup()
    while True:
        t1=threading.Thread(target=led_blink)
        t2=threading.Thread(target=func)
        t1.start()
        t2.start()
        t1.join()
        time.sleep(2)




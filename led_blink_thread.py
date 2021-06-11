import RPi.GPIO as GPIO
import time
import threading
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
# blinking function
GPIO.setup(37, GPIO.OUT) #pin numarasina gore
GPIO.setup(38, GPIO.OUT) #pin numarasina gore

global i
def func():
    i=0
    while True:
        time.sleep(1)
        i+=1
        print(i)

def led_setup():
    GPIO.output(37,GPIO.LOW)
    GPIO.output(38,GPIO.LOW)
def blink_high(pin):
    GPIO.output(pin,GPIO.HIGH)
def blink_low(pin):
    GPIO.output(pin,GPIO.LOW)

def led_blink(): 
    print("blink(37)",blink_high(37))
    time.sleep(0.1)
    print("blink(37)",blink_low(37))
    time.sleep(0.1)
    print("blink(37)",blink_high(37))
    time.sleep(0.1)
    print("blink(37)",blink_low(37))       
if __name__ == "__main__":
    led_setup()
    while True:
        t1=threading.Thread(target=led_blink)
        t1.start()
        t1.join()
        time.sleep(2)



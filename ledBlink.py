import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
# blinking function
GPIO.setup(37, GPIO.OUT) #pin numarasina gore
GPIO.setup(38, GPIO.OUT) #pin numarasina gore
GPIO.setup(40, GPIO.OUT) #pin numarasina gore
GPIO.setup(36, GPIO.OUT) #pin numarasina gore
GPIO.setup(33, GPIO.OUT) #pin numarasina gore
GPIO.setup(35, GPIO.OUT) #pin numarasina gore6
def led_setup():
    GPIO.output(37,GPIO.LOW)
    GPIO.output(38,GPIO.LOW)
    GPIO.output(40,GPIO.LOW)
    GPIO.output(33,GPIO.LOW)
    GPIO.output(35,GPIO.LOW)
    GPIO.output(36,GPIO.LOW)
def blink(pin):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(0.11)


def led_blink(): 
    for i in range(0,5):

        print("blink(37)",blink(37))
        time.sleep(1)
        print("blink(38)",blink(38))
        time.sleep(1)
        print("blink(40)",blink(40))
        time.sleep(1)
        print("blink(33)",blink(33))
        time.sleep(1)
        print("blink(35)",blink(35))
        time.sleep(1)
        print("blink(36)",blink(36))
        time.sleep(1)
led_setup()
led_blink()
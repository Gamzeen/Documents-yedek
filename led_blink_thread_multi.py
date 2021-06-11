import RPi.GPIO as GPIO
import time
import threading
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setwarnings(False)
GPIO.setup(37, GPIO.OUT) #pin numarasina gore
GPIO.setup(38, GPIO.OUT) #pin numarasina gore
GPIO.setup(40, GPIO.OUT) #pin numarasina gore
GPIO.setup(36, GPIO.OUT) #pin numarasina gore
GPIO.setup(33, GPIO.OUT) #pin numarasina gore
GPIO.setup(31, GPIO.OUT) #pin numarasina gore6
#irs led icin-----------------------------------
irs_role_tetik=0
irs_delta_zaman_asimi=0#bu kaldirilabilir
irs_okutuldu=0
sicaklik_yuksek=0
#-----------------------------------
#online led icin-----------------------------------
online_role_tetik=0
online_zaman_asimi=0#bu kaldirilabilir
online_okutuldu=0
kapi_gecis_izni_yok=0
#-----------------------------------
#offline led-----------------------------------
offline_role_tetik=0
offline_zaman_asimi=0#bu kaldirilabilir
offline_okutuldu=0
zamani_gecmis_barkod=0
kapi_gecis_izni_yok=0
#-----------------------------------
def led_setup():
    GPIO.output(37,GPIO.LOW)
    GPIO.output(38,GPIO.LOW)
    GPIO.output(40,GPIO.LOW)
    GPIO.output(36,GPIO.LOW)
    GPIO.output(33,GPIO.LOW)
    GPIO.output(31,GPIO.LOW)
def blink_high(pin):
    GPIO.output(pin,GPIO.HIGH)
def blink_low(pin):
    GPIO.output(pin,GPIO.LOW)
def led_blink(): 
    if irs_role_tetik==1:
        print("blink(37)",blink_high(37))
    if irs_role_tetik==0:
        print("blink(37)",blink_low(37))
    if irs_okutuldu==1:
        print("blink(38)",blink_high(38))
    if irs_okutuldu==0:
        print("blink(38)",blink_low(38))
    if sicaklik_yuksek==1:
        print("blink(40)",blink_high(40))
    if sicaklik_yuksek==0:
        print("blink(40)",blink_low(40))

    if online_role_tetik==1 or offline_role_tetik==1 :
        print("blink(36)",blink_high(36))
    if online_role_tetik==0 or offline_role_tetik==0:
        print("blink(36)",blink_low(36))
    if online_okutuldu==1 or offline_okutuldu==1:
        print("blink(33)",blink_high(36))
    if offline_role_tetik==0 or offline_okutuldu==0:
        print("blink(33)",blink_low(36))       
    if kapi_gecis_izni_yok==1 or zamani_gecmis_barkod==1:
        print("blink(31)",blink_high(33))
    if kapi_gecis_izni_yok==0 or zamani_gecmis_barkod==0:
        print("blink(31)",blink_low(33))
        
def func():
    global irs_okutuldu
    global zamani_gecmis_barkod
    while True:
        irs_okutuldu=1
        zamani_gecmis_barkod=1       
        time.sleep(3)
        irs_okutuldu=0
        zamani_gecmis_barkod=0
     
if __name__ == "__main__":
    led_setup()
    while True:
        t1=threading.Thread(target=led_blink)
        t2=threading.Thread(target=func)
        t1.start()
        t2.start()
        t1.join()
        time.sleep(2)

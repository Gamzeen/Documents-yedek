def mesafe_olc(b):
    mesafe=2
    if mesafe<10:
        a=1
        rf(a)
        #pass
    if b==1 and mesafe<10:
        print("role cagir")    
def rf(a):
    response=1
    if response==1:
        b=1
        mesafe=mesafe_olc(b)
    if a==1 and response ==1:
        print("role cagir")
        

print(mesafe_olc(2))
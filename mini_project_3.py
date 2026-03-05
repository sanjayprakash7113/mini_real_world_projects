a=input()
if len(a)==10 and a.isdigit():
    print("valid number")
else:
    if len(a)<10:
        print("num missing")
    else:
        print("num was only in 10 digit")


temp=input()
if temp.isdigit():
    temp=int(temp)
if temp < 18:
    print("Too Cold")
elif 18 <= temp <= 26:
    print("Comfortable")
else:
    print("Too Hot")    

pin=input()
if pin.isdigit():
    pin=int(pin)
    if pin==7112:
        print("enter your amount")
    else:
        print("wrong pin")
    pin=input()
    if pin.isdigit():
        pin=int(pin)
        if pin==7112:
            print("enter your amount")
        else:
            print("wrong pin you only have one chance")
        pin=input("last chance",)
        if pin.isdigit():
            pin=int(pin)
            if pin==7112:
                print("enter your amount")
            else:
                print("wrong pin again your account locked")


correct_pin = 7112
attempts = 0

while attempts < 3:
    pin = input("Enter PIN: ")

    if pin.isdigit():
        pin = int(pin)

        if pin == correct_pin:
            print("Enter your amount")
            break
        else:
            attempts += 1
            print("Wrong PIN")
    else:
        print("Invalid input")

if attempts == 3:
    print("Account locked")

        
        








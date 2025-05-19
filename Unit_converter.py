print("Unit Converter")
try:
    km = input("Enter the Km : ")
    km = float(km)
    choose = int(input("1. Miles\n2. Feet :  "))
    if choose == 1:
        print("The Km to Miles =",round(km * 0.621371 , 2))
    elif choose == 2:
        print("The km to Feet =",km * 3280.84)
except ValueError:
    print("Number only...")

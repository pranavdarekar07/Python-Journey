name = input("Enter your name : ")
age = int(input("Enter your age : "))
print(f"Hi your name is {name} and your age is {age}")
if age < 18:
    print(f"{name} you cannot vote until your are 21...")
else:
    print(f"{name} you can vote.")
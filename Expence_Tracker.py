print("Expence tracker application")
day_expence = []
while True:
    money = input("Add expence or type 'q' for quit... : ")
    if money == "q":
        break
    elif money.isdigit():
        day_expence.append(int(money))
    elif money.isalpha():
        print("Only number allowed")
    else:
        print("wrong input!!!")
print(day_expence)  
print(f"Total expence: ${sum(day_expence)}")
avg = sum(day_expence)/len(day_expence)
print(f"Average expence: ${avg}")
print(f"Highest expence: ${max(day_expence)}")
print(f"Entries : {len(day_expence)} items")

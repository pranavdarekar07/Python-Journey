print("Even / Odd Classifier (type 'q' to quit)")

while True:
    user = input("Enter a number: ")
    if user.lower() == "q":
        break
    try:
        num = int(user)          # convert once
    except ValueError:
        print("❌  Numbers only.")
        continue                 # ask again

    if num == 0:
        print("The number is zero.")
    elif num < 0:
        parity = "even" if num % 2 == 0 else "odd"
        print(f"The number {num} is negative {parity}.")
    else:                        # positive
        parity = "even" if num % 2 == 0 else "odd"
        print(f"The number {num} is positive {parity}.")

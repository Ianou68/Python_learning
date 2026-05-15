import random

x = random.randint(1, 100)

print("5 tries")

for i in range(5):
    a = int(input("Enter the code: "))

    if a < x:
        print("Higher")
    else:
        print("Lower")

    if a == x:
        print("The code is correct")
        break
    else:
        print("Incorrect code")

else:
    print(f"Out of attempts. The code was {x}.")

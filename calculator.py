# Simple Calculator - my first python project

print("----- CALCULATOR -----")

while True:
    print("")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose option (1-5): ")

    if choice == "5":
        print("Bye!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Wrong choice, try again")
        continue

    # taking numbers from user
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        print("Answer =", a + b)
    elif choice == "2":
        print("Answer =", a - b)
    elif choice == "3":
        print("Answer =", a * b)
    elif choice == "4":
        if b == 0:
            print("Cannot divide by zero")
        else:
            print("Answer =", a / b)

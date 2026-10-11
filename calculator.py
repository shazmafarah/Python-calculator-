
def calculator():
    print("MY PYTHON CALCULATOR")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    while True:
        choice = input("Choose an option (1-5): ")

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice!")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", a + b)
            elif choice == "2":
                print("Result:", a - b)
            elif choice == "3":
                print("Result:", a * b)
            elif choice == "4":
                if b == 0:
                    print("Cannot divide by zero!")
                else:
                    print("Result:", a / b)

        except ValueError:
            print("Please enter valid numbers.")

calculator()

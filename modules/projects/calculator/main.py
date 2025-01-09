if __name__ == "__main__":
    from operations import add, subtract, multiply, divide

    def menu():
        print("Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

    while True:
        menu()
        choice = input("Choose an operation (1-5): ")
        if choice == "5":
            print("Exiting Calculator. Goodbye!")
            break

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == "1":
            print("Result:", add(num1, num2))
        elif choice == "2":
            print("Result:", subtract(num1, num2))
        elif choice == "3":
            print("Result:", multiply(num1, num2))
        elif choice == "4":
            print("Result:", divide(num1, num2))
        else:
            print("Invalid choice. Please try again.")
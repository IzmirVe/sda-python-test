


def calculator():
    print("Simple Calculator Time!")
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                print("Error: Division by zero. Nice try!")
                return
            result = num1 / num2
        else:
            print("Invalid operator. Try again with +, -, *, or /.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("That's not a number! Please enter valid numbers.")


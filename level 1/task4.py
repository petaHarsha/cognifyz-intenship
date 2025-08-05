def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    elif operation == "%":
        if num2 == 0:
            return "Error: Modulo by zero"
        return num1 % num2
    else:
        return "Error: Invalid operation"

if __name__ == "__main__":
    print("Simple Calculator")
    try:
        operation = input("Enter operation (+, -, *, /, %): ").strip()
        if operation in ["+", "-", "*", "/", "%"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            result = calculator(operation, num1, num2)
            print("Result:", result)
        else:
            print("Error: Invalid operation selected.")
    except ValueError:
        print("Error: Please enter valid numbers.")

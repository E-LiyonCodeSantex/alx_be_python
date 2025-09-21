# Prompt to input value
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt to input operation method
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {int(result)}")
    case "-":
        result = num1 - num2
        print(f"The result is {int(result)}")
    case "*":
        result = num1 * num2
        print(f"The result is {int(result)}")
    case "/":
        if num1 == 0 or num2 == 0:
            result = "Cannot divide by zero."
            print(result)
        else:
            result = num1 / num2
            print(f"The result is {int(result)}")
    case _:
        result = "Invalid operation."


# Prompt to input value
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt to input operation method
operation = input("Choose the operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print(f"The result is {int(result)}.")
elif operation == "-":
    result = num1 - num2
    print(f"The result is {int(result)}.")
elif operation == "*":
    result = num1 * num2
    print(f"The result is {int(result)}.")
elif operation == "/":
    if num1 <= 0 or num2 <= 0:
        print("Cannot divide by zero.")
    else:
        result = num1 / num2
        print(f"The result is {int(result)}.")
else:
    print("Invalid operation.")

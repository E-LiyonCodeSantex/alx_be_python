class ValueTooHighError(Exception):
    """Exception raised when the input value is too high."""
    def __init__(self, value):
        self.value = value
        super().__init__(f"Value {value} is too high! Must be 100 or less.")

try:
    number = int(input("Enter a number: "))
    if number > 100:
        raise ValueTooHighError(number)
    else:
        print(f"Your number is {number}. All good!")
except ValueTooHighError as e:
    print("Custom Exception:", e)
except ValueError:
    print("Error: Please enter a valid integer.")

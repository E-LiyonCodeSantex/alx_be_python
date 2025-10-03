# Global vs Local Scope in Python
# Global scope
message = "Hello from global scope"

def greet():
    # Local scope
    message = "Hello from local scope"
    print("Inside function:", message)  # Uses local variable

# Call the function
greet()

# Outside the function
print("Outside function:", message)  # Uses global variable

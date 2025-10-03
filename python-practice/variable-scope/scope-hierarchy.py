# Scope Hierarchy (LEGB Rule)

# Global scope
value = "Global Value"

def outer_function():
    # Enclosing scope
    value = "Enclosing Value"

    def inner_function():
        # Local scope
        value = "Local Value"
        print("L - Local:", value)  # Local scope wins

    inner_function()
    print("E - Enclosing:", value)  # Enclosing scope

print("G - Global:", value)  # Global scope
outer_function()

# Built-in scope example
print("B - Built-in len():", len("Python"))  # Built-in function

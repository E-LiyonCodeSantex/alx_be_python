# Types of Scopes (LEGB Rule)
# where: L: Local, E: Enclosing, G: Global, B: Built-in

count = 10  # Global variable

def outer_function():
    # E: Enclosing scope
    count = 5  # Enclosing variable (local to outer_function)

    def inner_function():
        # L: Local scope
        count = 2  # Local variable (specific to inner_function)
        print(f"L - Inner function count: {count}")  # Uses local count (2)

        # B: Built-in scope
        print(f"B - Length of 'Python': {len('chinedu')}")  # Uses built-in len()

    inner_function()
    print(f"E - Outer function count: {count}")  # Uses enclosing count (5)

print(f"G - Global scope count: {count}")  # Uses global count (10)

outer_function()

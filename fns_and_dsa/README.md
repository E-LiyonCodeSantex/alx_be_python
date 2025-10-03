🧠 Functions, Data Structures, and Modules – Python Project
📚 Overview
This project is part of the ALX Back-End Web Development curriculum and focuses on mastering core Python programming concepts. You'll learn how to define and use functions, manipulate built-in data structures, and extend Python’s capabilities using modules and libraries.

🎯 Objectives
By completing this project, you will be able to:

Define and invoke Python functions using def and lambda.

Work with parameters, return values, and scope (local, global, nonlocal).

Apply the LEGB rule for variable resolution.

Manipulate data using Lists, Tuples, Sets, and Dictionaries.

Create and use custom modules.

Import and utilize standard and external libraries (e.g., requests, datetime).

Implement best practices for namespace and scope management.

📁 Repository Structure
Code
alx_be_python/
└── fns_and_dsa/
    ├── arithmetic_operations.py
    ├── shopping_list_manager.py
    ├── explore_datetime.py
    └── temp_conversion_tool.py
🧪 Tasks
0. Arithmetic Operations Function
File: arithmetic_operations.py

Goal: Define perform_operation(num1, num2, operation) to handle basic arithmetic.

Operations: add, subtract, multiply, divide (with zero-division handling).

Tested via: Provided main.py script.

1. Shopping List Manager
File: shopping_list_manager.py

Goal: Use a list to manage shopping items.

Features:

Add item

Remove item

View list

Exit

Interface: Menu-driven loop with input validation.

2. Explore datetime Module
File: explore_datetime.py

Goal: Use the datetime module to:

Display current date and time.

Calculate a future date based on user input.

Functions:

display_current_datetime()

calculate_future_date(days)

3. Temperature Conversion Tool
File: temp_conversion_tool.py

Goal: Convert temperatures between Celsius and Fahrenheit.

Global Variables:

FAHRENHEIT_TO_CELSIUS_FACTOR

CELSIUS_TO_FAHRENHEIT_FACTOR

Functions:

convert_to_celsius(fahrenheit)

convert_to_fahrenheit(celsius)

User Input: Temperature value and unit (C or F) with error handling.

🧠 Key Concepts Covered
Function definition and invocation

Parameter passing and return values

Scope and namespace resolution (LEGB)

Data structure operations

Module creation and usage

External library integration (pip install)

Input validation and error handling

✅ Completion Criteria
Each script must meet the functional requirements.

Code should be clean, readable, and modular.

All tasks are mandatory and contribute to your project score.
# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform basic arithmetic operations based on the operation parameter.

    Parameters:
    - num1 (float): First number
    - num2 (float): Second number
    - operation (str): One of 'add', 'subtract', 'multiply', 'divide'

    Returns:
    - float: Result of the arithmetic operation
    - str: Error message in case of division by zero
    """
    operation = operation.strip().lower()

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"

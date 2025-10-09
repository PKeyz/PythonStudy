"""
variables
"""
is_continuing = True
a = None
b = None
result = None

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

"""
What's the first Number?: INPUT
+-*/
Pick an operation: INPUT
What's the next number?: INPUT
3.0 * 5.0 = 15.0
Type 'y' to continue calculating with 15.0, or type 'n' to start a new calculation: INPUT
"""

def addition(a, b):
    """
    Taking two integers as inputs, adds them and returns a result value
    """
    result = a + b
    return result

def subtraction(a, b):
    """
    Taking two integers as inputs, subtracts them and returns a result value
    """
    result = a - b
    return result

def division(a, b):
    """
    Taking two integers as inputs, divides them and returns a result value
    """
    result = a / b
    return result

def multiplication(a, b):
    """
    Taking two integers as inputs, multiplies them and returns a result value
    """
    result = a * b
    return result
    
def calculate(a, b, operation):
    """
    Taking two integers and the operation string as inputs to calculate the result of the operation
    """
    is_calculating = True

    while is_calculating:
        if operation == "+":
            result = addition(a, b)
            return result
            is_calculating = False
        elif operation == "-":
            result = subtraction(a, b)
            return result
            is_calculating = False
        elif operation == "/":
            result = division(a, b)
            return result
            is_calculating = False
        elif operation == "*":
            result = multiplication(a, b)
            return result
            is_calculating = False
        else:
            is_proceeding = input("Wrong operation selected, press 'y' to continue, or any other button to cancel the program: ")
            if is_proceeding == "y":
                is_calculating = True
                return is_calculating
            else:
                is_calculating = False
                return is_calculating
            
print(logo)           

while(is_continuing):
    if a is None:
        a = int(input("What's the first number?: "))
    
    print("+\n-\n/\n*\n")
    operation = input("Pick an operation: ")
    b = int(input("What's the next number?: "))
    
    result = calculate(a, b, operation)

    print(f"{a} {operation} {b} = {result}")

    ask_to_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit: ")
    
    if ask_to_continue == "y":
        is_continuing = True
        a = result
        b = None 
        result = None
        
    else:
        is_continuing = False
        a = None
        b = None
        result = None
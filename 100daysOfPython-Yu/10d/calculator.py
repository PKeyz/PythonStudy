
def print_ascii_art():
    print("""
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
    """)
def ask_for_first_number() -> int:
    num_1 = int(input("What's the first number?: \n"))
    return num_1

def ask_for_next_number() -> int:
    num_2 = int(input("What's the next number?: \n"))
    return num_2

def ask_for_operator():
    operator = input("Pick an operation \n+\n-\n*\n/\n")
    return operator

def calculator(num1, operator, num_2) -> float:
    if operator == "+":
        result = num1 + num_2
    elif operator == "-":
        result = num1 - num_2
    elif operator == "*":
        result = num1 * num_2
    elif operator == "/":
        result = num1 / num_2
    return round(result,2)

def print_result(num_1, operator, num_2, result):
    print(f"{num_1} {operator} {num_2} = {result}")

def prompt_user_to_continue(result):
    user_prompt = input(f"Type 'y' to continue with {result}, or type 'n' to start new calculation, type ANY KEY to close the calculator:\n")
    return user_prompt

def empty_calculation():
    num_1 = ask_for_first_number()
    operator = ask_for_operator()
    next_num = ask_for_next_number()
    result = calculator(num_1, operator, next_num)
    print_result(num_1, operator, next_num, result)
    user_choice = prompt_user_to_continue(result)
    return result,user_choice

def succequent_calc(result):
    num_1 = result
    operator = ask_for_operator()
    next_num = ask_for_next_number()
    result = calculator(num_1, operator, next_num)
    print_result(num_1, operator, next_num, result)
    user_choice = prompt_user_to_continue(result)
    return result, user_choice

print("CALCULATOR APP")
calculate = True
print_ascii_art()
result,user_choice = empty_calculation()

while calculate:
    if user_choice == "y":
       result, user_choice = succequent_calc(result)
    elif user_choice == "n":
        result,user_choice = empty_calculation()
    else:
        calculate = False

# #CLAUDE EXAMPLE
# def calculator_app():
#     print("CALCULATOR APP")
#
#     result = None
#
#     while True:
#         # Get first number (or use previous result)
#         if result is None:
#             num_1 = ask_for_first_number()
#         else:
#             num_1 = result
#
#         operator = ask_for_operator()
#         next_num = ask_for_next_number()
#         result = calculator(num_1, operator, next_num)
#         print_result(num_1, operator, next_num, result)
#
#         user_choice = prompt_user_to_continue(result)
#
#         if user_choice == "y":
#             continue  # Keep result for next iteration
#         elif user_choice == "n":
#             result = None  # Reset for new calculation
#         else:
#             break  # Exit calculator
#
#
# calculator_app()
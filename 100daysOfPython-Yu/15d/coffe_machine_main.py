from numpy.random.mtrand import choice

#ENUMS
WATER                   = "water"
MILK                    = "milk"
COFFEE                  = "coffee"
PRICE                   = "price"
MONEY                   = "money"
ESPRESSO                = "Espresso"
LATTE                   = "Latte"
CAPPUCCINO              = "Cappuccino"
REPORT                  = "Report"
OFF                     = "Off"
VALUE                   = "value"
PENNY                   = "Penny"
NICKEL                  = "Nickel"
DIME                    = "Dime"
QUARTER                 = "Quarter"
PROVIDER_TEL            = "+01526374"

menu = {
    "Espresso":{
        "water" :   50,
        "milk"  :   0,
        "coffee":   18,
        "price" :   1.5
        },
    "Latte": {
        "water" :   200,
        "milk"  :   150,
        "coffee":   24,
        "price" :   2.5
        },
    "Cappuccino":{
        "water" :   250,
        "milk"  :   100,
        "coffee":   24,
        "price" :   3
        }
}

machine_resources = {
    "water" :   500,
    "milk"  :   200,
    "coffee":   100,
    "money" :   200
}

monetary_value = {
    "Quarter"   :   {"value" : 0.25},
    "Dime"      :   {"value" : 0.1},
    "Nickel"    :   {"value" : 0.05},
    "Penny"     :   {"value" : 0.01},
}

MACHINE_RUNNING = True

# 2. Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.
def shut_down_machine(has_resources:bool):
    """Shut down the machine"""
    resources = has_resources
    if not resources:
        global MACHINE_RUNNING
        MACHINE_RUNNING = False

# 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
def send_report():
    """Prints machine resources report to console"""
    print(f"Water: {machine_resources[WATER]}ml\nMilk: {machine_resources[MILK]}ml\nCoffee: {machine_resources[COFFEE]}g\nMoney: ${machine_resources[MONEY]}:")

# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.
def ask_user_choice():
    """Ask the user to choose an option"""
    user_input = input(f"What would you like? ({ESPRESSO}/{LATTE}/{CAPPUCCINO}):\n").capitalize()
    return user_input

def get_user_choice_resources(user_input):
    """Main user choice interface function for menu selection, report and shutdown"""
    user_choice = user_input
    if user_input not in (ESPRESSO, LATTE, CAPPUCCINO, REPORT, OFF):
        print("Please enter either 'espresso','latte' or 'cappuccino'.")
    elif user_choice == REPORT:
        send_report()
    elif user_choice == OFF:
        keep_running = False
        shut_down_machine(keep_running)

# 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.

def insufficient_resources_feedback(user_input):
    """Print statements for def check sufficient_resources"""
    if machine_resources[WATER] <= menu[user_input][WATER]:
        print("Sorry, there is not enough water.\n")
    elif machine_resources[MILK] <= menu[user_input][MILK]:
        print("Sorry, there is not enough milk.\n")
    elif machine_resources[COFFEE]<= menu[user_input][COFFEE]:
        print("Sorry, there is not enough coffee.\n")



def check_sufficient_resources(user_input):
    """Checks if machine has sufficient resources to  produce user selection"""
    if (user_input == REPORT) or (user_input == OFF):
        pass
    elif  (machine_resources[WATER]>= menu[user_input][WATER]) and (machine_resources[MILK] >= menu[user_input][MILK]) and (machine_resources[COFFEE] >= menu[user_input][COFFEE]):
        return True
    else:
        insufficient_resources_feedback(user_input)
        return False

def deduct_machine_resources(user_input):
    machine_resources[WATER] -= menu[user_input][WATER]
    machine_resources[MILK] -= menu[user_input][MILK]
    machine_resources[COFFEE] -= menu[user_input][COFFEE]

# 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
def print_price(user_input):
    """Payment prompt to the user with exact price of selection"""
    print(f"Please insert ${menu[user_input][PRICE]}")

# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
def calculate_user_payment():
    user_quarters   = float(input(f"How many {QUARTER}s?: "))
    user_dimes      = float(input(f"How many {DIME}s?: "))
    user_nickles    = float(input(f"How many {NICKEL}s?: "))
    user_pennies    = float(input(f"How many {PENNY}s?: "))
    user_payment = (user_quarters * float(monetary_value[QUARTER][VALUE])) + (user_dimes * float(monetary_value[DIME][VALUE])) + (user_nickles * float(monetary_value[NICKEL][VALUE])) + (user_pennies * float(monetary_value[PENNY][VALUE]))
    return user_payment

def process_payment(user_payment,user_input):
    if user_payment >= menu[user_input][PRICE]:
        machine_resources[MONEY] += menu[user_input][PRICE]
        print(f"Thank you! Your {user_input} will the brewed in a second =)")
        return True
    else:
        print(f"Sorry, ${user_payment} is not enough. A {user_input} costs ${menu[user_input][PRICE]}.")
        return False

def process_refund(user_payment, user_input):
    surplus = user_payment - menu[user_input][PRICE]
    refund = surplus
    total_sum = 0
    if machine_resources[MONEY] < refund:
        machine_resources[MONEY] -= refund
        print(f"Sorry, there is not enough money to refund the full sum.\n please take {machine_resources[MONEY]} and call {PROVIDER_TEL} to get the full sum.")
    elif machine_resources[MONEY] >= refund:
        for coin,coin_info in monetary_value.items():
            coin_value = coin_info[VALUE]
            if refund >= coin_value:
                coin_count = int(refund // coin_value)
                coin_sum = coin_count * coin_value
                refund -= coin_value * coin_count
                machine_resources[MONEY] -= coin_sum
                total_sum += coin_sum
                #print(f"Your refund is ${coin_sum} in {coin_count} {coin} coins.")
            else:
                coin_count = 0
                #print(f"Your refund is ${coin_sum} in {coin_count} {coin} coins.")
    print(f"Your refund is ${total_sum}.")

# 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.

# 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink


user_input = ask_user_choice()
get_user_choice_resources(user_input)
has_sufficient_resources = check_sufficient_resources(user_input)
shut_down_machine(has_sufficient_resources)
user_payment = calculate_user_payment()
is_payment_accepted = process_payment(user_payment,user_input)

process_refund(user_payment,user_input)



# while MACHINE_RUNNING:
#     user_choice_resources = get_user_choice_resources()
#     print(user_choice_resources)
#     enough_resources_bool = check_sufficient_resources(user_choice_resources)
#     # if enough_resources_bool:
#     #     print_price(user_choice_resources)
#     #     # process_payment(user_choice_resources)
#     #     # deduct_machine_resources(user_choice_resources)















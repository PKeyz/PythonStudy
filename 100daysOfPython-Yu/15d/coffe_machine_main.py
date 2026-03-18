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

monetary_value = {
    "Penny"     :   {"value" : 0.01},
    "Nickel"    :   {"value" : 0.05},
    "Dime"      :   {"value" : 0.1},
    "Quarter"   :   {"value" : 0.25}
}

machine_resources = {
    "water" :   50,
    "coffee":   100,
    "milk"  :   200,
    "money" :   0
}


ON = True

#TODO
# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.

def ask_user_choice():
    """Ask the user to choose an option"""
    user_input = input("What would you like? (espresso/latte/cappuccino):\n")
    return user_input

def get_user_choice_resources(choice):
    #choice = ask_user_choice()
    if choice == "espresso":
        resource_list = [menu["Espresso"]["water"],menu["Espresso"]["milk"],menu["Espresso"]["coffee"],menu["Espresso"]["price"]]
        return resource_list
    elif choice == "latte":
        resource_list = [menu["Latte"]["water"],menu["Latte"]["milk"],menu["Latte"]["coffee"],menu["Latte"]["price"]]
        return resource_list
    elif choice == "cappuccino":
        resource_list = [menu["Cappuccino"]["water"],menu["Cappuccino"]["milk"],menu["Cappuccino"]["coffee"],menu["Cappuccino"]["price"]]
        return resource_list
    elif choice == "report" or choice == "off":
        pass
    else:
        print("Please enter either 'espresso','latte' or 'cappuccino'.")




# 2. Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.
def shut_down_machine(user_input):
    """Shut down the machine"""
    if user_input == "off":
        global ON
        ON = False
    return ON

# 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
def send_report(user_input):
    if user_input == "report":
        print(f"Water: {machine_resources['water']}ml\nMilk: {machine_resources['milk']}ml\nCoffee: {machine_resources['coffee']}g\nMoney: ${machine_resources['money']}:")


# 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.
# def check_sufficient_resources():


# 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

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


user_choice = ask_user_choice()
user_choice_resources = get_user_choice_resources(user_choice)
# while ON:
#     pass
















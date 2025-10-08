#==========================================================================
#V.1
#==========================================================================
# bill = 0
# tip = 0
# num_people = 0
#
# print("Welcome to the tip calculator.")
#
# def count_payment():
#     global bill, tip, num_people
#
#     print("Welcome to the tip calculator!\n What was the total bill?")
#     bill = float(input())
#
#     print("How much tip would your like to give? 10,20, or 15?")
#     tip += int(input())
#
#     print("How many people to pay the bill?")
#     num_people = int(input())
#
# def count_tip():
#     payment_per_person = round((bill * (((float(tip))/10)+1) / num_people),2)
#     return print(f"Each person should pay: " + str(payment_per_person) )
#
# count_payment()
# count_tip()
#==========================================================================
#V.2
#==========================================================================
bill = 0
tip = 0
num_people = 0

def count_tip():
    global bill,tip,num_people
    print("Welcome to the tip calculator!\n What was the total bill?")
    bill = round(float(input()),2)

    print("How much tip would your like to give? 10,20, or 15?")
    tip = int(input())
    tip_options = [0,10,15,20]
    while tip not in tip_options:
        print("This percentage is not allowed! Try again")
        tip = int(input())

    print(f"You selected to tip {tip}%.\n Thank you!")

    print("How many people to pay the bill?")
    num_people = int(input())

def calculate_tip():
    payment_per_person = round(float(((bill * (tip/10))) /num_people),2)

    print(f"Each person should pay: {payment_per_person}" )

count_tip()
calculate_tip()
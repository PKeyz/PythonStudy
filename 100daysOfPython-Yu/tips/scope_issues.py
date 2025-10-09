bill = 0  # This is a GLOBAL variable
tip = 0   # This is also GLOBAL

def count_payment():
    bill = float(input())  # This is a LOCAL variable (different from global)
    tip = int(input())     # This is also LOCAL (different from global)
    return bill, tip

# Now you capture the returned values
bill, tip = count_payment()  # This OVERWRITES the global variables with returned values

#=======================================================================
#=======================================================================
total_bill = 0
tip_percent = 0

def count_payment():
    bill = float(input())  # Different name inside!
    tip = int(input())
    return bill, tip

total_bill, tip_percent = count_payment()  # Works fine!

#=======================================================================
#=======================================================================


# Instead of modifying globals
def count_payment():
    global bill, tip
    bill = float(input())
    tip = int(input())


# Consider returning
def count_payment():
    bill = float(input())
    tip = int(input())
    return bill, tip


bill, tip = count_payment()





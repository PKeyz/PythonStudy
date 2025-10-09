def pizza_calculator():
    cost = 0

    size = input("What size of pizza do you want? S, M, or L:\n")
    pepperoni = input("Do you want pepperoni on your pizza? Y or N:\n")
    extra_cheese = input("Do you want extra cheese? Y or N:\n")

    if size == "S":
        cost += 15

    elif size == "M":
        cost += 20
    else:
        cost += 25


    if pepperoni == "N":
        cost == cost
    elif pepperoni == "Y" and size == "S":
        cost += 2
    elif pepperoni == "Y" and size in ["M","L"]:
        cost += 3

    if extra_cheese == "N":
        cost = cost
    elif extra_cheese == "Y":
        cost += 1

    print(f"You have ordered a Pizza of size {size}, with {pepperoni} pepperoni and {extra_cheese} extra cheese.\n"
          f"The price of the pizza is {cost}")

pizza_calculator()
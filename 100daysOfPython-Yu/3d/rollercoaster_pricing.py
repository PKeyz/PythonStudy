def rollercoaster():

    height = float(input("What is your height?\n"))

    cost = 0

    if height < 120 :
        print("Sorry you are too short to have fun.")
    else:
        age = float(input("What is your age?\n"))

        photo = input("Do you want a photograph?\n")
        if photo == "yes":
            cost += 3

        if  age < 12 :
            cost += 5
            print(f"You have to pay {cost}")
            print("Have a good ride!")

        elif 12 < age < 18:
            cost += 7
            print(f"You have to pay {cost}")
            print("Have a good ride!")
        else:
            cost += 12
            print(f"You have to pay {cost}")
            print("Have a good ride!")

rollercoaster()
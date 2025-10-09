import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
round = 0
user_count = 0
computer_count = 0
while (user_count <= 2) and (computer_count <= 2):

        #user_count !=3 or computer_count != 3):
    print(f"Round {round}: User: {user_count} - Computer: {computer_count}")
    user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))

    computer_input = random.randint(0,2)

    if (user_input == 0 and computer_input == 0) or (user_input == 1 and computer_input == 1) or (user_input == 2 and computer_input == 2):
        if user_input == 0:
            print(f"{rock}\n")
            print(f"Computer chose:\n {rock}\n")
            print("Its a draw!\n")
        elif user_input == 1:
            print(f"{paper}\n")
            print(f"Computer chose:\n {paper}\n")
            print("Its a draw!\n")
        elif user_input == 2:
            print(f"{scissors}\n")
            print(f"Computer chose:\n {scissors}\n")
            print("Its a draw!\n")
        round += 1
        user_count = user_count
        computer_count = computer_count

    elif (user_input == 0 and computer_input == 2) or (user_input == 1 and computer_input == 0) or (user_input == 2 and computer_input == 1) :
        if user_input == 0:
            print(f"{rock}\n")
            print(f"Computer chose:\n {paper}\n")
            print("The User wins!\n")
        elif user_input == 1:
            print(f"{paper}\n")
            print(f"Computer chose:\n {rock}\n")
            print("The User wins!\n")
        elif user_input == 2:
            print(f"{scissors}\n")
            print(f"Computer chose:\n {paper}\n")
            print("The User wins!\n")
        round += 1
        user_count += 1

    elif (computer_input == 1 and user_input == 0) or (computer_input == 0 and user_input == 2) or (
                computer_input == 2 and user_input == 1):
        if user_input == 0:
            print(f"{rock}\n")
            print(f"Computer chose:\n {paper}\n")
            print("The Computer wins!\n")
        elif user_input == 1:
            print(f"{paper}\n")
            print(f"Computer chose:\n {rock}\n")
            print("The Computer wins!\n")
        elif user_input == 2:
            print(f"{scissors}\n")
            print(f"Computer chose:\n {paper}\n")
            print("The Computer wins!\n")
        round += 1
        computer_count += 1

        print(f"User won {user_count} times, Computer won {computer_count} times! Congratulations, the user wins!")

    if user_count == 3:
        print(f"User won {user_count} times, Computer won {computer_count} times! The User wins! Congratulations!")
    elif computer_count == 3:
        print(f"User won {user_count} times, Computer won {computer_count} times! The Computer wins, maybe next time!")


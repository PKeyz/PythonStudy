import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the secret auction program.")

bidders = {} 
next_bidder = "yes"
highest_key = " "
highest_value = 0

while (next_bidder == "yes"):
  name = input("What is your name? ")
  bid_amount = int(input("What's your bid? : $"))

  if highest_value < bid_amount:
    highest_key = name
    highest_value = bid_amount
  
  bidders[name] = bid_amount
  next_bidder = input("Are there any other bidders? Type 'yes' or 'no' ")
  if (next_bidder == "yes"):
    os.system('cls' if os.name == 'nt' else 'clear')
  else:
    print(f"The highest bidder is {highest_key} with a bid of ${highest_value}")
    #iterate over dict values
    #compare values until highes found
    #retrieve key and value
    #print highest key and value "The winner is [key] with a bid of $[value]."
print(bidders)
   
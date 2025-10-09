#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input(f"How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#1.take sum of all elements
#2.define array length with 1.
#3.define random iterators of lengths of each element
#4.create counter = 0 and count up in a loop to length of password array
#5.put each element into their own array []
#6.have a random number decide which it is if nr_x != 0 (initial numeric input is it's own counter variable)
#7.if counter <= len(password array) and nr_x != 0 roll a new random symbol from this specific list and insert at passwort[counter]
#8.also counter += 1 and nr_x -= 1
#9.if counter <= len(password) or (nr_x == 0 and nr_y.....) str(print(f"{password)")

#add more elif cases to catch the None continues, when the counters get to 0... e.g
#just choose another case  if random_element == x and x == 0 , roll again
#


#1.
nr_elements = nr_letters + nr_numbers + nr_symbols

#2.
password = [None] * nr_elements

#4. seems unnecessary atm
counter = 0


for counter in range (0,len(password)):
  while password[counter] is None:  
  #6.
    element_array = ["letters","numbers","symbols"]
    random_element = random.randint(0,2)
  
    #3.
    random_letter_index = random.randint(0,len(letters)-1)
    random_number_index = random.randint(0,len(numbers)-1)
    random_symbol_index = random.randint(0,len(symbols)-1)
    
    if element_array[random_element] == "letters" and nr_letters != 0:
      l = letters[random_letter_index]
      password[counter] = l
      nr_letters -= 1
      
    elif element_array[random_element] == "numbers" and nr_numbers != 0:
      n = numbers[random_number_index]
      password[counter] = n 
      nr_numbers -= 1
      
    elif element_array[random_element] == "symbols" and nr_symbols != 0:
      s = symbols[random_symbol_index]
      password[counter] = s
      nr_symbols -= 1
      
    else:
      continue

#test print
password_string = "".join(password)

print(f"{password_string}")

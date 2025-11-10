# import random
#
# numbers = ["0","1","2","3","4","5","6","7","8","9"]
# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# symbols = ["!", "@", "#", "$", "%", "&", "*", "(", ")", "_"]
#
# password_seed = [numbers,letters,symbols]
#
# passwort_length = int(input("How long should the password be?\n"))
#
# include_numbers = int(input("Should it include numbers. NO = 0, or YES = 1\n"))
# include_letters = int(input("Should it include letters. NO = 0, or YES = 1\n"))
# include_symbols = int(input("Should it include symbols. NO = 0, or YES = 1\n"))
#
# user_choice = [include_numbers, include_letters, include_symbols]
#
# final_password = ""
#
# if user_choice == [0,0,0]:
#     print("Password must contain at least one category.")
# elif user_choice == [0, 0, 1]:
#     while len(final_password) < passwort_length:
#         random_elem = random.randint(0,len(symbols)-1)
#         final_password += password_seed[2][random_elem]
# elif user_choice == [0, 1, 0]:
#     while len(final_password) < passwort_length:
#         random_elem = random.randint(0, len(letters) - 1)
#         final_password += password_seed[1][random_elem]
# elif user_choice == [1, 0, 0]:
#     while len(final_password) < passwort_length:
#         random_elem = random.randint(0, len(numbers) - 1)
#         final_password += password_seed[0][random_elem]
# elif user_choice == [1, 1, 0]:
#     while len(final_password) < passwort_length:
#         choice=[0,1]
#         random_elem = random.choice(choice)
#         final_password += password_seed[random_elem][random.randint(0,len(password_seed[random_elem])-1)]
# elif user_choice == [0, 1, 1]:
#     while len(final_password) < passwort_length:
#         choice = [1, 2]
#         random_elem = random.choice(choice)
#         final_password += password_seed[random_elem][random.randint(0, len(password_seed[random_elem])-1)]
# elif user_choice == [1, 0, 1]:
#     while len(final_password) < passwort_length:
#         choice = [0, 2]
#         random_elem = random.choice(choice)
#         final_password += password_seed[random_elem][random.randint(0, len(password_seed[random_elem])-1)]
# elif user_choice == [1, 1, 1]:
#     while len(final_password) < passwort_length:
#         choice = [0, 1, 2]
#         random_elem = random.choice(choice)
#         final_password += password_seed[random_elem][random.randint(0, len(password_seed[random_elem])-1)]
# else:
#     print("Instructions unclear, please try again!")
# # for range in (1, passwort_length):
#
# print(final_password)


import secrets
import string

# Get user preferences
password_length = int(input("How long should the password be? "))

include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
include_letters = input("Include letters? (y/n): ").lower() == 'y'
include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

# Build character pool based on choices
char_pool = ""
if include_numbers:
    char_pool += string.digits
if include_letters:
    char_pool += string.ascii_letters  # includes both upper and lowercase
if include_symbols:
    char_pool += "!@#$%&*()_"

# Validate
if not char_pool:
    print("Password must contain at least one category.")
else:
    # Generate password
    password = ''.join(secrets.choice(char_pool) for _ in range(password_length))
    print(f"Your password: {password}")

#KEY TAKEAWAYS:
#1 Version: Too complicated, too many lines of code, too many cases - not functional
#2 Version: Solving variation via boolean options added to a list of characters
#           randomly adding symbols from resulting list to final password
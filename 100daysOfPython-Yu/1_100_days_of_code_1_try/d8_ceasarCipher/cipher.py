import art

#TODO-1:DONE: Import and print the logo from art.py when the program starts.

#TODO-2:DONE: What if the user enters a shift that is greater than the number of letters in the alphabet?

#TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the Code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
#maybe use a do while loop!

#Try running the program and entering a shift number of 45.
#Add some Code so that the program continues to work even if the user enters a shift number greater than 26.
#Hint: Think about how you can use the modulus (%).

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
working = "yes"

shift = shift % 26
if shift == 0:
    shift += 1

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(text, shift, direction):
    text_list = list(text)
    cipher_array = []
    cipher_text = ""

    if direction == "encode":
    
        for x in text_list:
            index = alphabet.index(x)
            y = alphabet[index + shift]
            cipher_array += y
        
        cipher_text = "".join(cipher_array)
        print(f"The encoded text is {cipher_text}")
            
    elif direction == "decode":
        
        for x in text_list:
            index = alphabet.index(x)
            y = alphabet[index - shift]
            cipher_array += y

        cipher_text = "".join(cipher_array)
        print(f"The encoded text is {cipher_text}")
    else:
        print("INPUT WRONG, TRY AGAIN!")
    
    working = input("Type 'yes', if you want to go again. Otherwise type 'no'\n").lower()

    if (working == "yes"):
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        shift = shift % 26
        if shift == 0:
            shift += 1
        
        caesar(text,shift,direction)

caesar(text,shift,direction)

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
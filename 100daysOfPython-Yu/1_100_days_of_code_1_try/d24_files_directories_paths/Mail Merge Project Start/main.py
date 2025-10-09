#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#list of all names to invite
invited_names_list = []
with open("Input/Names/invited_names.txt", 'r') as invited_names:
    for line in invited_names.readlines():
        name = line.strip('\n')
        invited_names_list.append(name)

#print(invited_names_list)

#first line from the default invitation
first_letter_line = []

#whole letter in a list, by line
default_letter = []
with open("Input/Letters/starting_letter.txt", 'r') as starting_letter:
    for line in starting_letter.readlines():
        default_letter.append(line)

first_letter_line = default_letter[0].partition('[name]')
#print(first_letter_line)

#converts tuple to list lst
lst = [*first_letter_line]

for name in invited_names_list:
    # delete 0-th line, which is the line in first_letter_line
    default_letter.pop(0)

    lst[1] = name

    default_letter.insert(0, lst[0] + lst[1] + lst[2])

    #prints letter names to the console
    print(default_letter)
    with open(f'./Output/ReadyToSend/invitation_{name}.txt', 'w+') as invitations:
        #adds the text line by line, because it has to be type str, and write(default_letter) is a lst[str] and returns an error
        for line in default_letter:
            invitations.write(line)

# #This is the courses short code... compared to mine above
# PLACEHOLDER = '[name]'
#
# with open("./Input/Names/invited_names.txt") as names_file:
#     names = names_file.readlines()
#
# with open("./Input/Letters/starting_letter.txt") as letter_file:
#     letter_contents = letter_file.read()
#     for name in names:
#         strinpped_name = name.strip()
#         new_letter = letter_contents.replace(PLACEHOLDER, strinpped_name)
#         with open(f"./Output/ReadyToSend/letter_for_{strinpped_name}.txt", 'w') as completed_letter:
#             completed_letter.write(new_letter)
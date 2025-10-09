def check_even_number():
    print("Insert number 1")
    num_1 = float(input())
    print("Insert number 2")
    num_2 = float(input())
    result = num_1 % num_2
    if result == 0 :
        print("Even number")
    else:
        print("Odd number")

check_even_number()
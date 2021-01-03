''' 
Created on: 2021/1/2
Last Updated: 2021/1/3
Various custom-coded data structures and algorithms

@author: Kyle
'''

import random as r

sort_functions = []

def bubble_sort(random_numbers):
    do_sort = True
    while do_sort:
        do_sort = False # Reset for this round
        for n in range(len(random_numbers)):
            if (n + 1) < len(random_numbers) and random_numbers[n] > random_numbers[n+1]:
                random_numbers[n], random_numbers[n+1] = random_numbers[n+1], random_numbers[n]
                do_sort = True
    
    return str(random_numbers)

def validate(user_choice):
    is_valid = False
    try:
        val = int(user_choice)
        if val > 0 and val < (len(sort_functions) + 1):
            is_valid = True
    except ValueError:
        print("Please choose a valid number from the options table.")
    return is_valid

def main():
    r.seed(None)
    qty = 10
    sort_functions.append(bubble_sort)
    print("Select a sort option:")
    for i in range(len(sort_functions)):
        print(str(i + 1) + ") " + sort_functions[i].__name__)
    user_choice = input()
    if(validate(user_choice)):
        random_numbers = r.sample(range(1,100), qty)
        print("Input: " + str(random_numbers))
        print("Output: " + sort_functions[int(i-1)](random_numbers))
    

if __name__ == "__main__":
    main()
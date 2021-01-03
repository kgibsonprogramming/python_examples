''' 
Created on: 2021/1/2
Last Updated: 2021/1/3
Various custom-coded data structures and algorithms

@author: Kyle
'''

import random as r

def bubble_sort(random_numbers):
    # Bubble sort is highly inefficient and rarely used in practice
    # Its main utility is a simple introduction to sorting algorithms
    do_sort = True
    while do_sort:
        do_sort = False # Reset for this round
        for n in range(len(random_numbers)):
            if (n + 1) < len(random_numbers) and random_numbers[n] > random_numbers[n+1]:
                random_numbers[n], random_numbers[n+1] = random_numbers[n+1], random_numbers[n]
                do_sort = True
    return str(random_numbers)

def insertion_sort(random_numbers):
    # Insertion sort is both simple and efficient for small or mostly sorted lists
    # It sees use in more complex sorting algorithms like Timsort
    # Compared to selection sort - another simple sorting algorithm - insertion is
    # usually the preferred choice due to fewer comparisons and its performance when
    # data is already mostly sorted
    i = 1
    while i < len(random_numbers):
        j = 1
        while j > 0 and random_numbers[j-1] > random_numbers[j]:
            random_numbers[j], random_numbers[j-1] = random_numbers[j-1], random_numbers[j]
            j -= 1
        i += 1
    return str(random_numbers)
    
def validate(user_choice, sort_functions):
    is_valid = False
    try:
        val = int(user_choice)
        if val > 0 and val <= (len(sort_functions)):
            is_valid = True
    except ValueError:
        print("Please choose a valid number from the options table.")
    return is_valid

def main():
    r.seed(None)
    qty = 10
    
    sort_functions = [bubble_sort, insertion_sort]
    print("Select a sort option:")
    for i in range(len(sort_functions)):
        print(str(i + 1) + ") " + sort_functions[i].__name__)
    user_choice = input()
    result = validate(user_choice, sort_functions)
    if(result == True):
        random_numbers = r.sample(range(1,100), qty)
        print("Input: " + str(random_numbers))
        print("Output: " + sort_functions[int(i-1)](random_numbers))
    else:
        print("Invalid input; exiting...")
    

if __name__ == "__main__":
    main()
''' 
Created on: 2021/1/2
Last Updated: 2021/1/5
Various custom-coded data structures and algorithms

@author: Kyle
'''

import random as r
from math import floor

def bubble_sort(random_numbers):
    # Bubble sort is highly inefficient and rarely used in practice
    # Its main utility is a simple introduction to sorting algorithms
    print("Entering bubble sort...")

    do_sort = True
    while do_sort:
        do_sort = False # Reset for this round
        for n in range(len(random_numbers)):
            if (n + 1) < len(random_numbers) and random_numbers[n] > random_numbers[n+1]:
                random_numbers[n], random_numbers[n+1] = random_numbers[n+1], random_numbers[n]
                do_sort = True
    return random_numbers

def insertion_sort(random_numbers):
    # Insertion sort is both simple and efficient for small or mostly sorted lists
    # It sees use in more complex sorting algorithms like Timsort
    # Compared to selection sort - another simple sorting algorithm - insertion is
    # usually the preferred choice due to fewer comparisons and its performance when
    # data is already mostly sorted
    print("Entering insertion sort...")

    i = 1
    while i < len(random_numbers):
        j = i
        while j > 0 and random_numbers[j-1] > random_numbers[j]:
            random_numbers[j], random_numbers[j-1] = random_numbers[j-1], random_numbers[j]
            j -= 1
        i += 1
    return random_numbers
    
def selection_sort(random_numbers):
    # Selection sort is another simple, efficient option for short lists
    # While generally the insertion sort is favored over the selection,
    # it can sort a list in no more than n swaps, making it a useful choice when
    # the swap operation is expensive. As an in-place sorting algorithm, it is also
    # conservative with memory use
    print("Entering selection sort...")
    
    for i in range(len(random_numbers)):
        minIdx = i
        for j in range(i+1, len(random_numbers)):
            if random_numbers[j] < random_numbers[minIdx]:
                minIdx = j
        if minIdx != i:
            random_numbers[i], random_numbers[minIdx] = random_numbers[minIdx], random_numbers[i]
    return random_numbers

def merge_sort(random_numbers):
    # A stable, efficient, comparison-based sort developed by John von Neumann
    # This example is a 'bottom-up' implementation of merge sort:
    # The first pass sorts a sub-list of length 2, the second a sub-list of 4, etc.
    # Note the additional memory overhead of merge sort, as it uses a second
    # work arrayfor the sorting process
    print("Entering merge sort...")
    
    work_array = [0 for _ in range(len(random_numbers))]
    i = 1
    while i < len(random_numbers):
        j = 0
        for j in range(0,len(random_numbers), j + (2 * i)):
            do_merge(random_numbers, j, min(j + i, len(random_numbers)), min(j + 2 * i, len(random_numbers)), work_array)
        # This copy prepares for the next iteration
        random_numbers = work_array.copy()
        i += i
    return random_numbers

def do_merge(a, iL, iR, iE, work_array):
    i = iL
    j = iR
    for k in range(iL, iE):
        if i < iR and (j >= iE or a[i] <= a[j]):
            work_array[k] = a[i]
            i += 1
        else:
            work_array[k] = a[j]
            j += 1
    
def heap_sort(random_numbers):
    # Think of heap sort as an improved selection sort. It iterates to take the largest/smallest
    # value and place it in the proper list position, making use of a heap data structure to
    # do this efficiently. The result is an improvement from O(n) in the selection sort to
    # O(n log n)
    print("Entering heap sort...")
    buildMaxHeap(random_numbers)
    end = len(random_numbers) - 1
    
    while end > 0:
        random_numbers[end], random_numbers[0] = random_numbers[0], random_numbers[end]
        end -= 1
        siftDown(random_numbers, 0, end)
    return random_numbers

def buildMaxHeap(random_numbers):
    start = getIParent(len(random_numbers) - 1)
    
    while start >= 0:
        siftDown(random_numbers, start, len(random_numbers) - 1)
        start -= 1

def siftDown(a, start, end):
    root = start
    
    while getILeftChild(root) <= end:
        child = getILeftChild(root)
        swapIdx = root
        
        if a[swapIdx] < a[child]:
            swapIdx = child
        if (child + 1) <= end and a[swapIdx] < a[child + 1]:
            swapIdx = child + 1
        if swapIdx == root:
            return
        else:
            a[swapIdx], a[root] = a[root], a[swapIdx]
            root = swapIdx

def getIParent(i):
    return floor((i - 1) / 2)

def getILeftChild(i):
    return 2*i + 1

def getIRightChild(i):
    return 2*i + 2
    
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
    
    sort_functions = [bubble_sort, insertion_sort, selection_sort, merge_sort, heap_sort]
    print("Select a sort option:")
    for i in range(len(sort_functions)):
        print(str(i + 1) + ") " + sort_functions[i].__name__)
    user_choice = input()
    result = validate(user_choice, sort_functions)
    if(result == True):
        random_numbers = r.sample(range(1,100), qty)
        print("Input: " + str(random_numbers))
        call_func = sort_functions[int(user_choice) - 1]
        print("Func to call: " + str(call_func))
        print("Output: " + str(call_func(random_numbers)))
    else:
        print("Invalid input; exiting...")
    

if __name__ == "__main__":
    main()
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

# o(n^2) solution

def twoSumBruteForce(list_of_numbers, target):
    for i, i_number in enumerate(list_of_numbers):
        for j, j_number in enumerate(list_of_numbers):
            if i == j:
                continue
            if i_number + j_number == target:
                return(i,j)
            
#Under o(n) solution    
def twoSum(list_of_numbers, target):
    previous_numbers = {}
    for current_index, current_number in enumerate(list_of_numbers):
        difference = target - current_number 
        if difference in previous_numbers:
            index_of_difference = previous_numbers[difference]
            return(current_index, index_of_difference)
        else: 
            previous_numbers[current_number] = current_index

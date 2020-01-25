"""
This file contains code for question 1 from chapter 1 in Cracking the Coding Interview

Question: Write a method to replace all spaces in a string with '%20'.
"""
import time
# My solution

def replace(string):
    """
    This method is used for replacing all the spaces in a string with '%20'
    Complexity: O(n^2)
    """
    string = string.rstrip()
    space_track = [False for _ in range(len(string))]
    for count, char in enumerate(string):
        if char == ' ':
            space_track[count] = True
    final_string = ''
    for count, item in enumerate(space_track):
        if item:
            final_string = final_string + '%20'
        else:
            final_string = final_string + string[count]
    return final_string

def replace_(string):
    """
    This method is used for replacing all the spaces in a string with '%20'
    Complexity: O(n)
    """
    string = string.rstrip()
    final_string = ''
    for char in string:
        if char == ' ':
            final_string += '%20'
        else:
            final_string += char
    return final_string

if __name__ == '__main__':
    start = time.time()
    print(replace('Siddhant is a good boy  '))
    print('[ANALYSIS] Time taken using method 1: {} seconds!'.format(round(time.time() - start, 5)))
    start = time.time()
    print(replace_('Siddhant is a good boy   '))
    print('[ANALYSIS] Time taken using method 1: {} seconds!'.format(round(time.time() - start, 5)))

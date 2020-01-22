"""
This file contains code for question 1 from chapter 1 in Cracking the Coding Interview

Question: Implement an algorithm to determine if a string has all unique characters.
"""
import pdb
# My solution

inp_string = 'abcdefghijkvlmnopqrstuvwxyz'

test_list = list()
for item in inp_string:
    if item in test_list:
        print('Repeated character found: ', item)
        exit()
    else:
        test_list.append(item)
print('The input test string contains no repeating chacaters!')

# Book Solution

def unique(string):
    if len(string) > 128:
        return False
    
    chars = [False for i in range(128)]
    for char in string:
        value = ord(char)
        # pdb.set_trace()        
        if chars[value] == True:
            return False
        # else:
        chars[value] = True
    return True


print(unique(inp_string))

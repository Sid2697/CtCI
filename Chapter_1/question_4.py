"""
This file contains code for question 1 from chapter 1 in Cracking the Coding Interview

Question: Given a string, write a function to check if it is a permutation of a palindrome.
"""
# This problem can be solved by checking if out of n words n - 1 is are repeated in even number and 1 is repeated in odd numbers


def palindrome(string):
    string = string.lower()
    string = string.replace(' ', '')
    freq_dict = dict()
    for char in string:
        if char not in freq_dict.keys():
            freq_dict[char] = 1
        else:
            freq_dict[char] += 1
    count_even = 0
    count_odd = 0
    for key, value in freq_dict.items():
        if value % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        if count_odd > 1:
            return False
    return True


if __name__ == '__main__':
    inp = 'Tact Cassdb'
    print(palindrome(inp))
"""
This file contains code for question 1 from chapter 1 in Cracking the Coding Interview

Question2 Given two strings, write a method to decide if one of is a permutation of the other.
"""
# My solution

def freq_dict(string):
    """
    This method is used to get the frequency dictionary of the input string
    """
    output_dict = dict()
    for char in string:
        if char not in output_dict.keys():
            output_dict[char] = 1
        else:
            output_dict[char] += 1
    return output_dict


def check(string1, string2):
    """
    Method for checking if string1 or string2 are permutation of each other.
    """
    string1_freq = freq_dict(string1)
    string2_freq = freq_dict(string2)
    if len(string1_freq) != len(string2_freq):
        return False
    for key in string1_freq.keys():
        if key not in string2_freq.keys():
            return False
        else:
            if string2_freq[key] == string1_freq[key]:
                continue
            else:
                return False
    return True


if __name__ == '__main__':
    print(check('dog', 'god'))


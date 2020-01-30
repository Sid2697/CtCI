"""
This file contains code for question 1 from chapter 1 in Cracking the Coding Interview

Question: Given two strings, write a function to check if they are one edit (or zero edit) away
"""

# My solution

def get_dict(str_):
    """
    This method is used to get the frequency dict of the input string
    """
    final_dict = dict()
    for item in str_:
        if item not in final_dict.keys():
            final_dict[item] = 1
        else:
            final_dict[item] += 1
    return final_dict


def swap_string(str_1, str_2):
    """
    This method is used to swap the two input strings
    """
    temp_str = str_2
    str_2 = str_1
    str_1 = temp_str
    return str_1, str_2


def one_away(str_1, str_2):
    """
    This method is used for knowing if one string is one edit distance away from the other.
    """
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    if len(str_1) < len(str_2):
        str_1, str_2 = swap_string(str_1, str_2)
    
    diff = len(str_1) - len(str_2)
    if diff < -1 or diff > 1:
        return False
    
    str_1_info = get_dict(str_1)
    str_2_info = get_dict(str_2)

    diff = 0
    for word, count in str_1_info.items():
        if word not in str_2_info.keys() and count > 1:
            return False
        elif word not in str_2_info.keys() and count == 1:
            diff += 1
        else:
            count_second = str_2_info[word]
            if count_second - count != 0:
                diff += 1
    
    if diff > 1:
        return False
    elif diff == 1:
        return True
    else:
        return "Same"


if __name__ == '__main__':
    output = one_away('sidd', 'sid')
    if not output:
        print('[FALSE] The strings are more than one edit distance away </3')
    elif output == "Same":
        print("[FLASE] The output are the same :)")
    else:
        print('[TRUE] The strings are one edit distance away!')

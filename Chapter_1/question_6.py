"""
This file contains code for question 1 from chapter 1 in Cracking the Coding Interview

Question: Implement a method to perform basic string compression using the counts of repeated characters, if the 'compressed' string is not
smaller than the original string, then the method should return the original string
"""
# My Solution


def compress(inp):
    """
    This method is used to compress the string
    inp: (string) uppercase or lowercase letters (a-z)
    """
    output_string = str()
    temp_count = 0
    last_char = None
    for char in inp:
        if last_char is None:
            last_char = char
            temp_count += 1
        elif last_char == char:
            last_char = char
            temp_count += 1
        else:
            output_string += last_char
            output_string += str(temp_count)
            last_char = char
            temp_count = 1
    output_string += last_char
    output_string += str(temp_count)
    if len(output_string) > len(inp):
        return inp
    return output_string



if __name__=='__main__':
    inp = 'aabcccccaaa'
    print(compress(inp))

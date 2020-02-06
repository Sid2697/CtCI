"""
This file contains code for question 7 from chapter 1 in Cracking the Coding Interview

Question: Rotate a NxN matrix by 90 degrees
"""
# My method
import pdb
import time
import numpy as np

def Rotate(original):
    """
    This method is for rotating an input square matrix by 90 degress
    original: (numpy.matrix) input matrix which is to be rotated
    """
    rows, columns = original.shape
    final = np.empty((rows, columns))
    for row in range(rows):
        row_transpose = np.transpose(original[row]).reshape(rows, 1)
        row_flip = np.flip(row_transpose).reshape(rows, 1)
        final[:, row] = row_flip.reshape(rows,)
    return final

    
if __name__ == "__main__":
    test = np.array(((1, 2, 3, 13),(4, 5, 6, 14), (7, 8, 9, 15), (10, 11, 12, 16)))
    # print('Input matrix: ', test)
    start = time.time()
    final_np = np.rot90(test)
    print(final_np)
    print('Time by Numpy', time.time() - start)
    start = time.time()
    final = Rotate(test)
    print(final)
    print('Time by me', time.time() - start)
    

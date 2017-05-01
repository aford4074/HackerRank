'''
Shape and Reshape

www.hackerrank.com/challenges/np-shape-reshape

python 2.7

Sample Input

1 2 3 4 5 6 7 8 9

Sample Output

[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''

import numpy as np

def hackerrank(l):
    return np.reshape(np.array(l, int), (3, 3))

print hackerrank(raw_input().split(' '))

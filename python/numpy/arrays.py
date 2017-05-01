'''
Arrays

www.hackerrank.com/challenges/np-arrays

Sample Input

1 2 3 4 -8 -10

Sample Output

[-10.  -8.   4.   3.   2.   1.]

python 2.7
'''

import numpy as np

def hackerrank(l):
    return np.array(l, float)[::-1]

print hackerrank(raw_input().split(' '))

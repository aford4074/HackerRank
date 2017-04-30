'''
Transpose and Flatten

www.hackerrank.com/challenges/np-transpose-and-flatten

python 2.7

Sample Input

2 2
1 2
3 4

Sample Output

[[1 3]
 [2 4]]
[1 2 3 4]
'''

import numpy as np

def hackerrank(l):
    a = np.array(l)

    print np.transpose(a)
    print a.flatten()

n, m = map(int, raw_input().split(' '))
l = [[row for row in map(int, raw_input().split(' '))] for rows in xrange(n)]

hackerrank(l)

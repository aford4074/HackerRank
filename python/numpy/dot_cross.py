'''
Dot and Cross

www.hackerrank.com/challenges/np-dot-and-cross

python 2.7

Sample Input

2
1 2
3 4
1 2
3 4

Sample Output

[[ 7 10]
 [15 22]]
'''

import numpy as np

n = int(raw_input())

a = np.array([raw_input().split(' ')[:n] for _ in xrange(n)], dtype = np.int)
b = np.array([raw_input().split(' ')[:n] for _ in xrange(n)], dtype = np.int)

print np.dot(a, b)

'''
Zeros and Ones

www.hackerrank.com/challenges/np-zeros-and-ones

python 2.7

Sample Input 0

3 3 3

Sample Output 0

[[[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]]

'''

import numpy as np

def hackerrank(l):
    print np.zeros(l, dtype = np.int)
    print np.ones(l, dtype = np.int)

hackerrank(map(int, raw_input().split(' ')))

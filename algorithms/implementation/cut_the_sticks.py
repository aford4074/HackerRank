'''
Cut the Sticks

www.hackerrank.com/challenges/cut-the-sticks

python 2.7

Sample Input 0

6
5 4 4 2 2 8

Sample Output 0

6
4
2
1
'''

import sys

def cut_sticks(arr):
    shortest = min(arr)

    return [stick - shortest for stick in arr if stick > shortest]

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

while arr:
    print len(arr)

    arr = cut_sticks(arr)

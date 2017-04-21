'''
Re.split()

www.hackerrank.com/challenges/re-split

Sample Input

100,000,000.000

Sample Output

100
000
000
000
'''

import re

def re_split(s):
    [print(number) for number in re.split(r'[,.]+', s) if number.isdigit()]

re_split(input())

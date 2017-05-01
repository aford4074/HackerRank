'''
Introduction to Regex Module

Sample Input

4
4.0O0
-1.00
+4.54
SomeRandomStuff

Sample Output

False
True
True
False
'''

def verify():
    inputs = ['4.0O0', '-1.00', '+4.54', 'SomeRandomStuff', '+-4.0', '', '4.-0', '+.2']
    answers = [False, True, True, False, False, False, False, True]

    for i, a in zip(inputs, answers):
        print(i, a, is_float(i))

import re

def is_float(float_str):
    try:
        float(float_str)

    except ValueError:
        return False

    return bool(re.match(r'(\+|\-)?[0-9]*[.][0-9]+$', float_str))

n = int(input())
for _ in range(n):
    print(is_float(input()))

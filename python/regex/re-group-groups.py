'''
Group, Groups & Groupdict

www.hackerrank.com/challenges/re-group-groups

Output Format

Print the first occurrence of the repeating character. If there are no repeating characters, print -1.

Sample Input

..12345678910111213141516171820212223
Sample Output

1
Explanation

.. is the first repeating character, but it is not alphanumeric.
1 is the first (from left to right) alphanumeric repeating character of the string in the substring 111.
'''

import re

def re_group_groups(s):
    m = re.search(r'([a-zA-Z0-9])\1', s)

    print(m.group(1) if m else '-1')

re_group_groups(input())

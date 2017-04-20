'''
ginortS

Sample Input

Sorting1234

Sample Output

ginortS1324
'''

from functools import cmp_to_key

def sort_cmp(a, b):
    if a == b:
        return 0

    # a_grp, b_grp = [1 if v.islower() else 2 if v.isupper() else 3 if int(v) % 2 else 4 for v in [a, b]]
    a_grp = 1 if a.islower() else 2 if a.isupper() else 3 if int(a) % 2 else 4
    b_grp = 1 if b.islower() else 2 if b.isupper() else 3 if int(b) % 2 else 4

    return -1 if a_grp == b_grp and a < b or a_grp < b_grp else 1

print(*(sorted(input(), key = cmp_to_key(sort_cmp))), sep = '')

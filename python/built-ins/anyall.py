'''
Any or All

Sample Input

5
12 9 61 5 14
Sample Output

True
'''

n = int(input())
l = input().split(' ')
print(all([int(s) > 0 for s in l]) and any([s == s[::-1] for s in l]))

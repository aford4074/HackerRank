'''
Standardize Mobile Numbers Using Decorators

www.hackerrank.com/challenges/standardize-mobile-number-using-decorators

python 2.7

3
07895462130
919875641230
9195969878

Sample Output

+91 78954 62130
+91 91959 69878
+91 98756 41230
'''

def wrapper(f):
    def fun(l):
        return f(['+91 ' + n[-10:-5] + ' ' + n[-5:] for n in l])

    return fun

@wrapper
def sort_phone(l):
    print '\n'.join(sorted(l))

if __name__ == '__main__':
    l = [raw_input() for _ in range(int(input()))]
    sort_phone(l)

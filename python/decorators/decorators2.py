'''
Decorators 2 - Name Directory

www.hackerrank.com/challenges/decorators-2-name-directory

python 2.7

Sample Input

3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F

Sample Output

Mr. Mike Thomson
Ms. Andria Bustle
Mr. Robert Bustle
'''

from operator import itemgetter

def person_lister(f):
    def inner(people):
        return [f(p) for p in sorted(people, key = itemgetter(2))]
        
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [raw_input().split() for i in range(int(raw_input()))]
    print '\n'.join(name_format(people))

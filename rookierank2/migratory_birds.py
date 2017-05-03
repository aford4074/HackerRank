'''
Migratory Birds

www.hackerrank.com/contests/rookierank-2/challenges/migratory-birds

python 2.7

Sample Input 0

6
1 4 4 4 5 3

Sample Output 0

4
'''

def hackerrank(birds):
    bird_types = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0
    }

    max_type = 1
    max_types = 0

    for bird in birds:
        bird_types[bird] += 1

        if bird_types[bird] > max_types:
            max_types = bird_types[bird]
            max_type = bird

        elif bird_types[bird] == max_types and bird < max_type:
            max_type = bird

    print max_type

n = int(raw_input())
birds = map(int, raw_input().split(' '))

hackerrank(birds)

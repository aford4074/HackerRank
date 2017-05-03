'''
Queens Attack 2

www.hackerrank.com/challenges/queens-attack-2

python 2.7
'''

def move_one(n, rq, cq, o, r, c):
    rq += r
    cq += c

    if rq == 0 or rq > n:
        return None, None

    if cq == 0 or cq > n:
        return None, None

    if (rq, cq) in o:
        return None, None

    return rq, cq

n, k = map(int, raw_input().split(' '))
RQ, CQ = map(int, raw_input().split(' '))

o = set([tuple(map(int, raw_input().split(' '))) for _ in xrange(k)])

attacks = 0

for r in (-1, 0, 1):
    for c in (-1, 0, 1):
        if (r, c) != (0, 0):
            rq, cq = RQ, CQ

            while rq:
                rq, cq = move_one(n, rq, cq, o, r, c)

                if rq:
                    attacks += 1

print attacks

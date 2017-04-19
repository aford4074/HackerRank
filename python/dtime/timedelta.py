import datetime

T = int(input())

format = '%a %d %b %Y %H:%M:%S %z'

for _ in range(T):
    dt1 = datetime.datetime.strptime(input(), format)
    dt2 = datetime.datetime.strptime(input(), format)

    print(abs(int(datetime.timedelta.total_seconds(dt1 - dt2))))

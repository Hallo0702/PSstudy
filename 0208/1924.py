day_month = [31,28,31,30,31,30,31,31,30,31,30,31]
x, y = map(int,input().split())
n = 1
day = 0
while n < x:
    day += day_month[n-1]
    n += 1

day += y-1
day %= 7

if day == 0:
    print("MON")
elif day == 1:
    print("TUE")
elif day == 2:
    print("WED")
elif day == 3:
    print("THU")
elif day == 4:
    print("FRI")
elif day == 5:
    print("SAT")
elif day == 6:
    print("SUN")
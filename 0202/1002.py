t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d = ((x1-x2)**2 + (y1-y2)**2)** 0.5

    # 1. 같은 원일 경우 2. 1곳에서 만날경우 3. 2곳에서 만날경우
    # 4. 안만날경우
    if r1 == r2 and d == 0:
        print(-1)
    elif r1 + r2 == d or abs(r1 - r2) == d:
        print(1)
    elif r1 + r2 > d and abs(r1-r2) < d:
        print(2)
    else:
        print(0)
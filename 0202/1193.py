x = int(input())
n = 1
cnt = 1

while n < x:
    n += cnt+1
    cnt += 1

if cnt % 2 == 1:
    a = 1
    b = cnt
    while n > x:
        a += 1
        b -= 1
        n -= 1
else :
    a = cnt
    b = 1
    while n > x:
        a -= 1
        b += 1
        n -= 1

print(f'{a}/{b}')

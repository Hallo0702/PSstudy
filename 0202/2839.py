n = int(input())
cnt = 0

while n % 5 != 0:
    cnt += 1
    n -= 3
    if n < 3 and n > 0:
        print('-1')
        break
else :
    print(cnt+(n//5))
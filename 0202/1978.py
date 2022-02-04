t = int(input())
cnt = 0

n = list(map(int, input().split()))

for m in n:
    if m == 1:
        pass
    else:
        for j in range(2,m):
            if m % j == 0:
                break
        else :
            cnt += 1

print(cnt)

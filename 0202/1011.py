t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    n = b-a
    tmp = 1
    while True:
        if n in range(tmp**2-tmp+1,tmp**2+1):
            print(2*tmp - 1)
            break
        elif n in range(tmp**2 + 1,tmp**2 + tmp):
            print(2*tmp)
            break
        else:
            tmp += 1

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    n = b-a
    tmp = 0
    while True:
        if n <= tmp*(tmp+1):
            break
        else:
            tmp += 1
    
    if n <= tmp**2:
        print(2*tmp - 1)
    else:
        print(2*tmp)
    
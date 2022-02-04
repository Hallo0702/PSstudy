while 1:
    a,b,c = map(int,input().split())
    if a == 0 and b == 0 and c == 0:
        break
    a = a**2
    b = b**2
    c = c**2
    sum = a+b+c
    large = max(a,b,c)
    sum = sum - large
    if sum == large:
        print('right')
    else:
        print('wrong')

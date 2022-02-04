t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    list_a = [j for j in range(1,n+1)] # 0층의 n까지 리스트
    for f in range(k): # k층을 찾기위해 k번 더함
        for idx in range(1,n):
            list_a[idx] += list_a[idx-1]
    print(list_a[n-1])
    


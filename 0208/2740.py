N, M = map(int, input().split())
A = []
for i in range(N):
    tmp = list(map(int,input().split()))
    A.append(tmp)

M, K = map(int, input().split())
B = []
for i in range(M):
    tmp = list(map(int,input().split()))
    B.append(tmp)


result = []

for i in range(N):
    tmp = []
    for j in range(K):
        num = 0
        for k in range(M):
            num += A[i][k]*B[k][j]
        tmp.append(num)
    result.append(tmp)

for i in range(N):
    for j in range(K):
        print(result[i][j],end=' ')
    print()

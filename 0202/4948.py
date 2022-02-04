list_tf = [True] * (123456*2+1)
lim = int(((123456*2)**0.5)+1)

for i in range(2,lim):
    if list_tf[i] == True:
        for j in range(i*2,123456*2+1,i):
            list_tf[j] = False
list_tf[0] = False
list_tf[1] = False

while 1 > 0:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for i in range(n+1,2*n + 1):
        if list_tf[i] == True:
            cnt += 1
    print(cnt)

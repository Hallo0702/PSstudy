m, n = map(int, input().split())
list_tf = [True] * (n+1)
lim = int((n**0.5)+1)

for i in range(2,lim):
    if list_tf[i] == True:
        for j in range(i*2,n+1,i):
            list_tf[j] = False
list_tf[0] = False
list_tf[1] = False
result = [x for x in range(m,n+1) if list_tf[x] == True]
for re in result:
    print(re)

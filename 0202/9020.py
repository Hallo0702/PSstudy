list_tf = [True] * (10000+1)
lim = int((10000**0.5)+1)

for i in range(2,lim):
    if list_tf[i] == True:
        for j in range(i*2,10000+1,i):
            list_tf[j] = False
list_tf[0] = False
list_tf[1] = False

list_prime = []
for i in range(10001):
    if list_tf[i] == True:
        list_prime.append(i)

t = int(input())
for i in range(t):
    n = int(input())
    s = n//2
    list_s = [x for x in list_prime if x <= s]
    list_s.reverse()
    for prime in list_s:
        a = prime
        b = n - prime
        if a in list_prime and b in list_prime:
            print(a,b)
            break
        
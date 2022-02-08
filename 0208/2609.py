a, b = map(int,input().split())
if a < b:
    a,b = b,a

def gcd(p,q):
    while q > 0:
        p, q = q, p%q
    return p

def lcm(n,m):
    return n*m // gcd(n,m)

print(gcd(a,b))
print(lcm(a,b))

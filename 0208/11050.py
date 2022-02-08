n, m = map(int, input().split())
up = 1
down = 1

for i in range(m):
    up *= n
    n -= 1

t = m
for i in range(m):
    down *= t
    t -= 1

print(up//down)
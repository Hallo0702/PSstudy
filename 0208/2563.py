area = [[0 for _ in range(101)] for _ in range(101)]

t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    for dx in range(x,x+10):
        for dy in range(y,y+10):
            area[dx][dy] = 1

cnt = 0
for i in range(101):
    for j in range(101):
        if area[i][j] == 1:
            cnt += 1

print(cnt)
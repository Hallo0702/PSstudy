# 받은 랜덤 n이 몇번째 줄에 있는지 찾는 문제입니다.
# 첫번재줄은 1 두번째줄은 1 + 6, 세번째 줄은 1 + 18, 네번째 줄은 1 + 36, 다섯번째 줄은 1+ 60까지입니다.
# 1, 1+6, 1+6+12,1+6+12+18,1+6+12+18+24 로 점점 늘어납니다.
cnt = 1
max = 1
n = int(input())

while max < n:
    max = max + 6*cnt
    cnt += 1

print(cnt)
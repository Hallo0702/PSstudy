import math

a,b,v = map(int, input().split())

# 만약 v/(a-b) 로 하면 올라갔다 내려오는 경우에는 하루가 더 ㄷ걸리게 된다.
# 그러므로 (v-b)/(a-b) 로 하면 내려와서 v-b보다 큰 경우는 통과한걸로 생각한다.

day = (v-b)/(a-b)
# 만약 소수인 경우는 올림처리를 해야한다.
print(math.ceil(day))
import math
R = int(input())
# 원의 넓이 = PI * R제곱
print(math.pi * R * R)
# 여기서 말하는 원은 대각선의 길이가 2R인 마름모의 넓이
# 1/2 * (2R)의 제곱 = 2*R*R
print(2*R*R)
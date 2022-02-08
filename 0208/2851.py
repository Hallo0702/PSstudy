score = []
for i in range(10):
    num = int(input())
    score.append(num)
result = [0]
for i in range(10):
    result.append(result[i]+score[i])
    if result[i+1] >= 100:
        cnt = i+1
        break
else:
    cnt = 10

if result[cnt] - 100 == 100 - result[cnt-1] :
    print(result[cnt])
elif result[cnt] - 100 < 100 - result[cnt-1]:
    print(result[cnt])
else:
    print(result[cnt-1])

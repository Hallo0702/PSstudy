num_list = []
result = []
for i in range(10001):
    num_list.append(i**2)
a = int(input())
b = int(input())
n = 1
while num_list[n] <= b:
    if num_list[n] >= a and num_list[n] <= b:
        result.append(num_list[n])
    n += 1


if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(result[0])


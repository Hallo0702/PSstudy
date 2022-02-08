n, m = map(int, input().split())
numbers = list(map(int, input().split()))
large = 0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            sum = numbers[i] + numbers[j] + numbers[k]
            if sum <= m:
                if large < sum:
                    large = sum

print(large)

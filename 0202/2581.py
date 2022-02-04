m = int(input())
n = int(input())
min = 0
sum = 0
for num in range(m,n+1):
    if num == 1:
        pass
    else:
        for i in range(2,num):
            if num % i == 0:
                break
        else :
            sum += num
            if min == 0:
                min = num

if min == 0:
    print(-1)
else : 
    print(sum)
    print(min)

N = int(input())
num_list = list(map(int,input().split()))
M = int(input())
tf_list = list(map(int, input().split()))

num_list.sort()

def mid(tf,num_list,left,right):
    if left > right:
        return 0
    m = (left+right)//2
    if num_list[m] == tf:
        return 1
    elif num_list[m] > tf:
        return mid(tf,num_list,left,m-1)
    else:
        return mid(tf,num_list,m+1,right)

for tf in tf_list:
    print(mid(tf,num_list,0,len(num_list)-1))


## set을 사용할 경우 시간이 빠르다!
## set을 이용한 코딩도 해볼것!
    


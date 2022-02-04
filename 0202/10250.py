# 아래층부터 채워나가는 문제
t = int(input())

for i in range(t):
    h,w,n = map(int, input().split())
    # 호수는 손님의 순서를 층의 수로 나눈 몫+1.(11 번손님은 10층짜리 건물에서 2번째 라인에 들어감)
    line = n//h + 1
    # 층수는 손님의 순서를 층수로 나눈 나머지
    floor = n % h
    # 10층짜리 건물에서 10번째 손님은 이 공식대로는 0층 2호에 있게 되는데 이경우는 따로해야함.
    if floor == 0:
        line = n//h
        floor = h
    print(f'{floor*100 + line}')
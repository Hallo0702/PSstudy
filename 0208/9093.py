t = int(input())
for i in range(t):
    words = list(input().split())
    for word in words:
        for j in range(len(word)):
            print(word[len(word)-j-1],end='')
        print('',end=' ')
    print()

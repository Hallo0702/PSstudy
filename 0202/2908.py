# 문자를 받아서 한문자당 해당 위치를 찾은 후 맞는 시간을 반환합니다.

word_list = [[],[],[],['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]

word = input()
time = 0
for w in word:
    for i in range(len(word_list)):
        if w in word_list[i]:
            time += i
            break

print(time)


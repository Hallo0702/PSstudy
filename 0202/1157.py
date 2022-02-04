# 가장 많이 나온 알파벳을 찾는 문제입니다.
# 대.소문자는 상관이 없습니다.
words= input().upper()
word = list(set(words))

cnt = []
for w in word:
    cnt.append(words.count(w))

if cnt.count(max(cnt)) > 1:
    print("?")
else :
    max = cnt.index(max(cnt))
    print(word[max])
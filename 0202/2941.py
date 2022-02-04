# 크로아티아 알파벳을 한 글자로 보고 문자의 길이를 측정한다
alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']

word = input()

for a in alpha:
    word = word.replace(a, '!')

print(len(word))
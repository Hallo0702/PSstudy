n = int(input())
cnt = 0
for i in range(n):
    word_list = []
    word = input()
    for i in range(len(word)-1):
        if word[i] in word_list:
            break
        else:
            if word[i] == word[i+1]:
                pass
            else:
                word_list.append(word[i])
    else:
        if word[len(word)-1] in word_list:
            pass
        else :
            cnt += 1

print(cnt)
    

            

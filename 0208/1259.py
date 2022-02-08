while 1:
    number = input()
    if number == '0':
        break
    else:
        num = []
        num.extend(number)
        for j in range(len(num)//2):
            if num[j] != num[-j-1]:
                print("no")
                break
        else:
            print("yes")
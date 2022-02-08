lit = list(map(int, input().split()))

if lit[0] == 1:
    for i in lit[1:7]:
        if lit[i] == lit[i-1]+1:
            pass
        else:
            print("mixed")
            break
    else:
        print("ascending")
elif lit[0] == 8:
    for i in lit[1:7]:
        if lit[i] == lit[i-1]-1:
            pass
        else:
            print("mixed")
            break
    else:
        print("descending")
else :
    print("mixed")
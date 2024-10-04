a1, a2, b1, b2 = int(input()), int(input()), int(input()), int(input())
if(a1 - 2 == b1 or a1 + 2 == b1):
    if(a2 + 1 == b2 or a2 - 1 == b2):
        print('YES')
    else:
        print('NO')
elif(a2 - 2 == b2 or a2 + 2 == b2):
    if(a1 + 1 == b1 or a1 - 1 == b1):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
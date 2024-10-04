a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if(a1 > a2):
    a1, b1, a2, b2 = a2, b2, a1, b1
if(a1 == a2):
    if(b1 == a1 or b2 == a1):
        print(a1)
    else:
        print(a1, min(b1, b2))
else:
    if(a2 > b1):
        print("Пустое множество")
    elif(a2 == b1):
        print(a2)
    elif(b2 <= b1):
        print(a2, b2)
    else:
        print(a2, b1)

        
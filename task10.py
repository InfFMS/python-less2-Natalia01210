a1, a2, b1, b2 = int(input()), int(input()), int(input()), int(input())
if(a1 + a2 == b1 + b2 or abs(a1 - a2) == abs(b1 - b2) or a1 == b1 or a2 == b2) :
    print("YES")
else:
    print("NO")
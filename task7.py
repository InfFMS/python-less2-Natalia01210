def F(now):
    if(n == 1):
        return False
    for i in range(2, int(now ** 0.5 // 1) + 1):
        if(now % i == 0):
            return False
    return True
n = int(input())
for i in range(2, n + 1):
    if(F(i)):
        print(i)
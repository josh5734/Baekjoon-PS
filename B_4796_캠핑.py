count = 1
while 1:
    maxDay = 0
    L, P, V = map(int, input().split(" "))
    if(L == 0 and P == 0 and V == 0):
        break
    fulluse = int(V / P) * L
    remnant = V - int(V / P) * P
    if(L <= remnant):
        maxDay += L
    else:
        maxDay += remnant
    maxDay += fulluse
    print("Case " + str(count)+": " + str(maxDay))
    count += 1

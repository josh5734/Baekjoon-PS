import math

n = int(input())
for i in range(n):
    H, W, Nth = map(int, input().split(" "))
    height = Nth % H

    if(height == 0):
        height = H

    distance = math.ceil(Nth / H)
    ans = str(height) + str(distance)

    if((len(str(height)) == 1 and len(str(distance)) == 1)
       or len(str(height)) == 2 and len(str(distance)) == 1):
        print(str(height) + "0" + str(distance))
    else:
        print(ans)


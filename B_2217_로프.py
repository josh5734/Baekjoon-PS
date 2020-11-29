number = int(input())
lopes = []

for i in range(number):
    lopes.append(int(input()))
lopes.sort(reverse=True)

cache = 0
for i in range(len(lopes)):
    weight = lopes[i] * (i+1)
    if(weight > cache):
        cache = weight
print(cache)

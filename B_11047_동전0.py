a, total = map(int, input().split(" "))
coins = []
for i in range(a):
    coins.append(int(input()))

# 4200 --> 1000 1000 1000 1000
coins = reversed(coins)
count = 0
for i in coins:
    if(total >= i):
        count += total // i
        total %= i
print(count)

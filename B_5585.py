change = 1000 - int(input())
answer = 0
coins = [500, 100, 50, 10, 5, 1]
for coin in coins:
    if(change >= coin):
        answer += change // coin
        change %= coin

print(answer)

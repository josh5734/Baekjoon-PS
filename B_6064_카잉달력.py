from math import gcd

def getLCM(x,y):
    return x * y // gcd(x,y)

tc = int(input())
for _ in range(tc):
    m,n,x,y = map(int, input().split())
    answer = -1

    # 달력의 마지막 해 
    last_year = getLCM(m,n)
    
    # 처음 x값이 되는 시점부터 m씩 증가시킨다.
    for year in range(x, last_year+1, m):
        # 아래 조건을 만족시키면 끝
        if (year - x) % m == 0 and (year-y) % n == 0:
            answer = year
            break

    print(answer)

from itertools import combinations as cb

N = int(input())
people = [i for i in range(1,N+1)]
power = [list(map(int, input().split())) for _ in range(N)]
team_comb = list(cb(people,N//2))
minValue = 100000
for team1 in team_comb:
    team2 = [x for x in people if x not in team1]

    p1, p2 = 0, 0
    for i,j in list(cb(team1,2)):
        p1 += power[i-1][j-1]
        p1 += power[j-1][i-1]
    
    for i,j in list(cb(team2,2)):
        p2 += power[i-1][j-1]
        p2 += power[j-1][i-1]
    difference = abs(p1-p2)

    if difference <= minValue:
        minValue = difference    
print(minValue)
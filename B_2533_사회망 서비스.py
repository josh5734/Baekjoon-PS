from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node):
    visited[node] = True
    dp[node][0], dp[node][1] = 0, 1

    for child in tree[node]:
        if not visited[child]:
            dfs(child) # 자식노드부터 처리한다.
            dp[node][0] += dp[child][1] # 내가 얼리어답터가 아닐 때
            dp[node][1] += min(dp[child][0], dp[child][1]) # 내가 얼리어답터일 때

n = int(input())
tree = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# dp[i][0] = 내가 얼리어답터가 아닐 때 필요한 친구의 수
# dp[i][1] = 내가 얼리어답터일 때 필요한 친구의 수
dp = [[0] * 2 for _ in range(n+1)]
visited = [False] * (n+1)
dfs(1)
print(min(dp[1][0], dp[1][1]))

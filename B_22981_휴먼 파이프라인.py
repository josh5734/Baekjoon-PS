import sys, math
input = sys.stdin.readline
n, k = map(int, input().split())
speed = list(map(int, input().split()))
speed.sort()

throuput = -1

# 1~(n-1)명이 같은 팀
for p in range(1, n):
    a = speed[0] * p
    b = speed[p] * (n - p)
    if throuput < a + b:
        throuput = a+b

if k % throuput:
    print(k//throuput + 1)
else:
    print(k//throuput)
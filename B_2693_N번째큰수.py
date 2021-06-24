import sys
if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        numbers = list(map(int, sys.stdin.readline().split())).sort(reverse=True)
        print(numbers[2])

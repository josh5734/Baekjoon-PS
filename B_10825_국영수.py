import sys
if __name__ == "__main__":
    n = int(input())
    student = []
    for _ in range(n):
        student.append(sys.stdin.readline().split())

    student = sorted(
        student, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
    for s in student:
        print(s[0])

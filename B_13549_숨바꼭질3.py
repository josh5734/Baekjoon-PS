from collections import deque


def search_sib(n, k):
    global time
    now = k
    while True:
        if now == n:
            break
        elif now // 2 < n:
            time += min(n - (now // 2), now - n)
            break
        else:
            if now % 2 == 0:
                now //= 2
            else:
                time += 1
                if ((now + 1) // 2) == n or ((now-1)//2) == n:
                    break
                elif ((now + 1) // 2) % 2 == 0:
                    now = (now+1) // 2
                else:
                    now = (now-1) // 2
                # q.append((now-1)//2)


if __name__ == "__main__":
    n, k = map(int, input().split())

    time = 0
    if n >= k:
        time = n-k
    else:
        search_sib(n, k)
    print(time)

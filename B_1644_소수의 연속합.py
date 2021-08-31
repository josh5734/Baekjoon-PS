# 에라토스테네스의 체
def prime_list(n):
    isPrime = [True] * (n+1)

    m = int(n ** 0.5)
    # n 제곱근 이하의 수에 대해서 i가 소수인 경우 i의 배수들은 소수가 아님
    for i in range(2, m + 1):
        if isPrime[i] == True:
            for j in range(i+i, n+1, i): 
                isPrime[j] = False

    # 소수 목록 리턴
    return [i for i in range(2, n+1) if isPrime[i] == True]


n = int(input())
answer = 0
prime_number = prime_list(n)

# 끝 포인터를 소수 집합의 맨 마지막에 놓고 시작
endCursor = len(prime_number) - 1
while endCursor >= 0:
    for startCursor in range(endCursor, -1, -1):

        # 연속된 소수의 합
        totalSum = sum(prime_number[startCursor:endCursor+1])
        if totalSum == n:
            answer += 1
        
        # 연속된 소수 합이 n보다 크면 끝 포인터를 왼쪽으로 이동
        elif totalSum > n:
            break

    endCursor -= 1
print(answer)

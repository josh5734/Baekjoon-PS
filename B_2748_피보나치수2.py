
# k번째 피보나치 수를 찾는 함수
def fibo(fib_list, kth):
    start_index = 2
    while(start_index <= kth):
        fibo_list.append(fibo_list[start_index-1]+fibo_list[start_index-2])
        start_index += 1
    return fibo_list[-1]


if __name__ == "__main__":
    # 0,1번째 피보나치 수 초기화
    first, second = 0, 1

    # 몇 번째 피보나치 수를 구하고자 하는가?
    k = int(input())

    # 피보나치 수를 저장할 리스트
    fibo_list = [first, second]

    answer = fibo(fibo_list, k)
    print(answer)

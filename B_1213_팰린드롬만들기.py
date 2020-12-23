from collections import Counter


if __name__ == "__main__":
    # 문자열 입력받기
    str = input()
    str_dic = Counter(str)

    # 각 단어의 개수가 홀수인 것이 2번 이상 나오면 palindrome 불가능
    odd_letter = ""
    odd_count = 0
    for v in str_dic:
        if str_dic[v] % 2 == 1:
            odd_letter = v
            odd_count += 1

    if odd_count >= 2:
        answer = "I'm Sorry Hansoo"
    else:
        sorted_dic = sorted(str_dic.items())

        # palindrome의 앞부분, 뒷부분
        front, end = "", ""
        for i in range(len(sorted_dic)):
            front += sorted_dic[i][0] * int(sorted_dic[i][1] / 2)
            end += sorted_dic[i][0] * int(sorted_dic[i][1] / 2)

        # 앞부분 + 홀수개수인 문자를 가운데에 하나 더 삽입 + 뒷부분 역순으로 정렬
        answer = front + odd_letter + end[::-1]
    print(answer)

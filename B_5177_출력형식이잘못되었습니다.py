import sys


if __name__ == "__main__":
    # 테스트 케이스의 수
    k = int(input())

    for n in range(k):
        # 최종적으로 문자열을 비교할 스택
        stack1 = [""]
        stack2 = [""]
        # 문자열 입력받고 모두 대문자로 변경
        str1 = list(sys.stdin.readline().strip().upper())
        str2 = list(sys.stdin.readline().strip().upper())

        # 같은 종류로 취급되는 특수문자를 변환
        for i in range(len(str1)):
            if str1[i] in ["(", "{", "["]:
                str1[i] = "("
            elif str1[i] in [")", "}", "]"]:
                str1[i] = ")"
            elif str1[i] in [",", ";"]:
                str1[i] = ","
        for i in range(len(str2)):
            if str2[i] in ["(", "{", "["]:
                str2[i] = "("
            elif str2[i] in [")", "}", "]"]:
                str2[i] = ")"
            elif str2[i] in [",", ";"]:
                str2[i] = ","

        # 특수문자 앞 뒤의 공백 처리 / 여러 번의 공백은 하나의 공백으로 처리
        for w in str1:
            # 연속되는 공백은 무시
            if stack1[-1] == ' ' and w == ' ':
                continue
            # 특수 문자 앞의 공백 무시
            elif stack1[-1] == ' ' and w in ['(', ')', ',', '.', ':']:
                stack1[-1] = w
            # 특수 문자 뒤의 공백 무시
            elif stack1[-1] in ['(', ')', ',', '.', ':'] and w == ' ':
                continue
            else:
                stack1.append(w)
        for w in str2:
            # 연속되는 공백은 무시
            if stack2[-1] == ' ' and w == ' ':
                continue
            # 특수 문자 앞의 공백 무시
            elif stack2[-1] == ' ' and w in ['(', ')', ',', '.', ':']:
                stack2[-1] = w
            # 특수 문자 뒤의 공백 무시
            elif stack2[-1] in ['(', ')', ',', '.', ':'] and w == ' ':
                continue
            else:
                stack2.append(w)

        if stack1 == stack2:
            print(f"Data Set {n+1}: equal")
            print()
        else:
            print(f"Data Set {n+1}: not equal")
            print()

import sys

if __name__ == "__main__":
    s, e, q = input().split()

    # 입장, 퇴장 시간 정보를 담고 있는 사전
    in_attendance = dict()
    out_attendance = dict()

    # 출석을 한 인원 수
    number = 0

    # 개강총회 시작, 종료, 스트리밍 종료 시간을 분 단위로 변환
    s = int(s[:2]) * 60 + int(s[-2:])
    e = int(e[:2]) * 60 + int(e[-2:])
    q = int(q[:2]) * 60 + int(q[-2:])

    # EOF 입력 받기
    while True:
        try:
            log = sys.stdin.readline().split()
            time = int(log[0][:2]) * 60 + int(log[0][-2:])
            name = log[1]
            # 입장 시간이 개강 총회 이전이면 정상 입장 처리
            if time <= s:
                in_attendance[name] = time
            # 퇴장 시간이 개강 총회 종료와 스트리밍 종료 사이에 있으면 정상 퇴장 처리
            if time >= e and time <= q:
                out_attendance[name] = time

        except:
            break

    for k in in_attendance:
        if k in out_attendance:
            number += 1
    print(number)

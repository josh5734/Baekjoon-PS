n, L = map(int, input().split(" "))
count = 0
water = list(map(int, input().split(" ")))
water = sorted(water)

# 누수된 곳의 시작과 끝점 정보를 튜플로 만들기
water_tape = []
for i in range(len(water)):
    x = (water[i] - 0.5, water[i] + 0.5)
    water_tape.append(x)

# 누수된 곳을 다 고칠때까지 while문 반복
while(len(water_tape) != 0):
    count += 1  # 테이프 개수 추가
    curr = water_tape[0][0]  # 시작점
    for x in water_tape:
        if curr + L >= x[1]:
            water_tape = water_tape[1:] # x가 위 조건을 만족하면 그거를 삭제.. 
            if(len(water_tape) == 0): #탈출조건
                break
print(count)

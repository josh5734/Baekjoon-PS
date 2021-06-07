# 처음에 Greedy라고 생각 -> X
# 6111로 가려고하는데 사용 가능한 버튼이 5, 6, 9라면 맨처음에 6을 찍으면 안 됌!

from itertools import product

channel = input()
m = int(input())
buttons = list(str(i) for i in range(10))
if m > 0: 
    broken_buttons = list(input().split())
    for x in broken_buttons:
        buttons.remove(x)
    
if m == 10:
    print(abs(int(channel) - 100))

else:
    min_dist = abs(int(channel) - 100) 

    # 이동하고자 하는 채널의 길이만큼 모든 순열을 구해보자.
    button_permutations = []
    for i in range(1, len(channel) + 1):
        button_permutations = list(product(buttons, repeat = i ))


        # +, - 버튼만 눌러서 이동하는 거리
        for c in button_permutations:
            move_channel = ''.join(c)
            distance_by_jumping = abs(int(move_channel) - int(channel)) + len(move_channel)
            if distance_by_jumping <= min_dist:
                min_dist = distance_by_jumping
    
    if '0' in buttons and len(buttons) >= 2:
        n = buttons[1] + '0' * len(channel)
        if abs(int(channel) - int(n)) + len(channel) + 1 < min_dist:
            min_dist = abs(int(channel) - int(n)) + len(channel) + 1
    elif len(buttons) >= 1:
        n = buttons[0] * (len(channel) + 1)
        if abs(int(channel) - int(n)) + len(channel) + 1 < min_dist:
            min_dist = abs(int(channel) - int(n)) + len(channel) + 1
    
    print(min_dist)

# 절대값 힙 210926
""" 
가설: 하얀색 캔버스에 가로 또는 세로 끝까지 닿는 검은 줄을 긋는다.
그리고 이렇게 완성된 그림이 있다면 최소한의 횟수를 알고 싶다.
만약 이 가설이 틀린 케이스라면 출력은 -1이 된다.
가설이 맞는 케이스에서는 그은 선들도 출력하는데
width 부분은 +1~W
h 부분은 -1~-h로 표현
0 은 흰색 1은 검은색

입력 
3 4
1 0 1 0
1 1 1 1
1 1 1 1
출력
4
1 3 -2 -3
"""
import sys
input = sys.stdin.readline
m, n = map(int, input().split())
canvas = [list(map(int, input().split())) for _ in range(m)]
canvas_t = list(map(list, zip(*canvas)))
# Transpose 를 해서 역방향도 계산 쉽게 해보자

# 일단 가설이 맞는지 검정해야하는데.. 
# 1. w부분으로 1을 만나면 h끝까지 1인지 검사
# 2. h 부분으로 1을 만나면 w 끝까지 1인지 검사 둘중 하나라도 틀리면 가설이 틀린다.
# 이렇게 가설을 검사하는 동시에 그어진 줄의 갯수와 해당 인덱스+1 값 가로로 그어진 글에는 -(인덱스 + 1) 를 저장하고 가설이 맞을 때는 전부 출력시키기
# 가설이 변경됨 1을 발견할 때 (첫 인덱스만 돌려도 될것 같음) 한쪽면은 전부 1이여야 True이다 만약 양쪽에 0이 존재하는 1이 있다면 False

count = 0
width_idx = [] # 입력할 때 +1
height_idx = [] # 입력할 때 +1, *-1
# 출력 width->height 인덱스 순
def is_right(canvas):
    # 0이 존재하는 인덱스를 찾기 => width가 1로만 이뤄지지 않은 곳
    # 여기선 0번째 row가 가지고 있는데.. canvas_t에서 0이 존재하는곳에 겹치는 값이 나오면 False
    zeros = []
    for i in range(m):
        if 0 in canvas[i]:
            zeros.append(i)
    for i in range(n):
        if 0 in canvas_t[i]:
            if i in zeros:
                return False
    return True


# 조건에 맞으면 아래를 출력
if is_right(canvas) == False:
    print(-1)
elif is_right(canvas):
    for i in range(n):
        if 0 in canvas_t[i]:
            continue
        else:
            count += 1
            width_idx.append(i + 1)
    for i in range(m):
        if 0 in canvas[i]:
            continue
        else:
            count += 1
            height_idx.append(-(i + 1))
    print(count)        
    print(*width_idx, *height_idx)
    
"""
3 3
1 1 1
1 0 1
1 1 1
출력
4
1 3 -1 -3
"""

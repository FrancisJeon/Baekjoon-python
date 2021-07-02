""" 210617 12:44 항해 20번 시간초과 """
""" stdin으로 바꿔서 제출해봤다. 여전히 시간초과 """
# 2차원 평면 위의 점 N개 좌표를 낮은 y좌표를 가진 점부터 출력 같은 y값을 가진 경우 더 낮은 x좌표 먼저 출력하는 프로그램
# 입력값
# 점의 갯수 n줄
# 점의 좌표 - n개

# 정렬 순서 = y좌표가 가장 작은곳부터 같을 때는 x좌표가 낮은게 우선
import sys
n = int(sys.stdin.readline())

x_coor = []
y_coor = []
new_x_coor = []
new_y_coor = []
temp_x = []
temp_y = []

# x = [1, 2]
# y = [1, 3]
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    x_coor.append(x)
    y_coor.append(y)

while y_coor:
    min_y = min(y_coor)
    while min_y in y_coor: 
        """ 좌표값 담아둔 곳 빌때까지 하고 있는데 좌표값 같은곳 끼리 따로 처리시켜야한다"""
        i = y_coor.index(min_y)
        temp_x.append(x_coor[i])
        temp_y.append(y_coor[i])
        del x_coor[i]
        del y_coor[i]

    temp_x.sort()
    # sort(temp_y)
    [new_x_coor.append(i) for i in temp_x]
    [new_y_coor.append(i) for i in temp_y]
    temp_x = []
    temp_y = []

for i in range(len(new_x_coor)):
    print(f'{new_x_coor[i]} {new_y_coor[i]}')

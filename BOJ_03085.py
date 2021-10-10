# 사탕 게임 211006
""" 
N * N 크기의 사탕을 입력받은 뒤, 색이 다른 두칸을 골라서 교환한다.
교환 후, 같은색으로 된 가장 긴 행 또는 열의 사탕 개수를 고르자.

* 알고리즘
1. 바꿀 때 가장 긴 길이를 만들 수 있는 방법을 떠올려보자. 
---> 만약 하나의 행 또는 열이 가득찬 상태로 이뤄졌다면 교환에만 지장 없을 경우 그 길이가 정답이다.
------> 즉 가장 길게 연결된 행 또는 열을 찾는게 목표
---> 가장 길게 연결된 하나의 길이를 발견할 경우 그 길이의 양 끝 상하좌우에 같은 색이 있는지 찾아야한다.
------> 기존의 그래프와 Transpose된 그래프를 이용해서 길이를 구하면 같은 함수를 사용할 수 있지만 메모리가 2배가 된다.
------> Transpose 없이 할 경우에는 행, 열에 대한 알고리즘을 별도로 코드로 짜두기
---> 문제는 중간이 비어있는 케이스에 옆으로 옮기면 가장 길어지는 경우인데 예제 3번과 같은 형태이다.

2. 브루트포스에 걸맞게 가능한 모든 swap을 진행한 뒤, N이 나오면 리턴 나머지는 모두 진행해보기
---> 왼쪽과 위는 확인할 필요 없고 우측과 하단만 확인하고 교환 상태와 기존 상태의 차이점인 부분은 교환이 진행된 두개의 행과 하나의 열 또는 두개의 열과 하나의 행(메모리 절약)

3. 2번을 N-1, N-1 구간에서 반복해서 최대값을 갱신하기
# n-1, n-1을 계산하기보다는 Transpose 된 상태로 각각 비교하는게 더 빠르겠다. (candy[n][n]을 계산하지 않는 경우 방지)
# 처음부터 끝까지 진행하면서 자기보다 우측과 하단의 원소를 비교해서 다르면 뒤집어진 array 생성하는 함수가 필요하다. -> 생성이 아니라 바뀐 위치의 max값만 구하면 된다. 기존의 max와 차이가 존재하기는 함..

4. 1-3을 합쳐서 중복 줄이는 방법
swap을 처음부터 끝까지 진행시키면서 swap 할 때 마다 관련된 3개 (행+열)의 연속된 길이를 구한다.

* list 내부의 원소 'c' 'c' 'p' 의 경우 swap 해도 정상적인 새 리스트가 만들어진다?? 풀이를 보니 다들 이 방식으로 풀이했다.
"""
# 풀이 시도 
'''
n = int(input())
candy = [list(input()) for _ in range(n)]
candy_t = list(map(list, zip(*candy)))
# Transpose 된 사탕
max_candy = 0

# 최대 사탕 길이 반환하는 함수 - 처음에는 전부를 다 구하는 방식으로 만들었는데 변화가 발생한 행과 열만 해당하도록 함수 변경
# 기존 방식은 [n][n] 부분까지 바꾸지 않는 방식으로 만들어져서 방법을 바꾸기로 했다. c, r 둘다 진행하는데 index 상태를 보고 둘중 하나는 진행하지 않기로
def get_max_candy_c(array, row, col): # 좌우
    global n
    cur_max, is_swap = 0, 0
    # 1. 열 swap - 같지 않으면 swap하지 않음
    if array[row][col] != array[row][col+1]:
        array[row][col], array[row][col+1] = array[row][col+1], array[row][col]
        is_swap = 1
    # 스왑여부 상관없이 max 계산
    temp = 1
    for i in range(n-1):
        if array[row][i] == array[row][i+1]:
            temp += 1
        else:
            cur_max = max(temp, cur_max)
            temp = 1
    cur_max = max(temp, cur_max)    
    # swap 원래대로 되돌리기 - 이것도 함수 내부에서 사용하면 상관 있을지는 모르겠다.
    if is_swap == 1:
        array[row][col], array[row][col+1] = array[row][col+1], array[row][col]
    return cur_max

def get_max_candy_r(array, row, col): # 상하
    global n
    cur_max, is_swap = 0, 0
    # 2. 행 swap
    if array[row][col] != array[row+1][col]:
        array[row][col], array[row+1][col] = array[row+1][col], array[row][col]
        is_swap = 1
    temp = 1
    for i in range(n-1):
        if array[i][col] == array[i+1][col]:
            temp += 1
        else:
            cur_max = max(temp, cur_max)
            temp = 1
    cur_max = max(temp, cur_max)
    if is_swap == 1:
        array[row][col], array[row+1][col] = array[row+1][col], array[row][col]
    return cur_max

# swap후 max 계산
'''

# 인터넷 답 긁어온거
import sys
input = sys.stdin.readline

def check(a, s_row, e_row, s_col, e_col):
    n = len(a)
    result = 1
    for i in range(s_row, e_row+1):
        cnt = 1
        for j in range(1, n):
            if a[i][j-1] == a[i][j]: cnt += 1
            else: cnt = 1
            # result = max(cnt, result) # max 함수를 쓰면 코드 가독성은 증가하지만 속도가 단축할까? 2/3로 감소한다. (유의미하다고 생각)
            if result < cnt: result = cnt
    for i in range(s_col, e_col+1):
        cnt = 1
        for j in range(1, n):
            if a[j-1][i] == a[j][i]: cnt += 1
            else: cnt = 1
            # result = max(cnt, result)
            if result < cnt: result = cnt
    return result

n = int(input())
a = [list(input().rstrip()) for _ in range(n)]
result = 0

# 매 포인트마다 좌우 상하 교환을 진행하는데 위치에 따라서 진행하지 않아도 되는 부분이 같이 담겨있다.
for i in range(n):
    for j in range(n):
        if j < n-1:
            a[i][j], a[i][j+1] = a[i][j+1], a[i][j] # 좌우 교환
            temp = check(a, i, i, j, j+1) # 연속부분 체크
            # result = max(result, temp)
            if result < temp: result = temp
            a[i][j], a[i][j+1] = a[i][j+1], a[i][j] # 원위치
        if i < n-1:
            a[i][j], a[i+1][j] = a[i+1][j], a[i][j] # 상하 교환
            temp = check(a, i, i+1, j, j)
            # result = max(result, temp)
            if result < temp: result = temp
            a[i][j], a[i+1][j] = a[i+1][j], a[i][j]
        if result == n: print(result); exit() # 결과가 n과 같을 경우 더이상 진행하는 의미가 없다.
print(result)

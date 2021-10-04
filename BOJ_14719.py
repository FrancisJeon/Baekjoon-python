# 빗물 210929
""" 
* 기둥이 존재하는지 파악하는 알고리즘
1. 왼쪽 -> 오른쪽 지나면서 다음 인덱스의 높이가 더 낮은곳이 있다면 그곳이 기둥 후보, 마지막 인덱스의 경우 무조건 후보에 넣어주자
2. 오른쪽 -> 왼쪽 지나면서 1번과 마찬가지로 더 낮은곳을 만나는 기둥 후보를 담아두자.
3. L->R, R->L 후보를 set를 사용해서 기둥들을 잡아준 다음
4. 기둥들 사이의 숫자들을 기둥만큼 채워주면 물의 양을 계산 할 수 있다. 물이 쌓일수 있는 최대 높이는 min(좌, 우 높이)

입력 
H W 주어진다.
블록이 쌓인 높이인 0이상 H이하 정수가 주어진다.

* 문제 알고리즘
1. 만약.. 기둥이 0개 또는 1개만 존재한다면 물을 담을 수 없다.
2. 기둥을 찾는다. 2개 이상의 기둥이 존재해야 하고 기둥은 전부 리스트에 담아준다.
2-1. 1번의 경우와 같지만 기둥이 두개 존재하는 경우, 두개의 기둥이 바로 옆으로 붙어있는 케이스는 물은 담을 수 없다. 이를 후보를 이용해서 겹치지 않는 형태임을 이용해서 기둥이 존재하지 않는것 처럼 처리할 수 있다.
예) 0230, 0220
# h3,w6 / 2 1 0 0 2 1 -> p1은 0,1,4,5 p2는 4, 0이 담겨야한다.
# h3,w6 / 0 0 2 2 3 0 -> p1은 4,5 p2는 4, 2, 0 => 기둥이 4 한개만 생성된다.
3. 두개 이상의 기둥이 존재해야 다음 단계로 갈 수 있고 아닐경우 0 return한다. 
물이 담긴다면 두 기둥 중 더 낮은 높이가 물이 담길수 있는 최고 높이
1번과 3번에 기둥이 존재한다면 2번에서 현재 높이와 최소 기둥높이 사이에 물을 가득 채운 값을 담으면 된다.
# 4 8 / 3 2 1 2 1 0 3 2 -> 답 9, 출력 4
중간의 기둥이 좌 우 보다 낮을경우 무시해야 한다.. 그런데 이게 방법이 어렵다.
"""

# 1, 내가 사용한 알고리즘 (반례: 중간에 기둥이 낮은게 존재할 경우 무시해야 한다)
'''
h, w = map(int, input().split())
array = list(map(int, input().split()))

# 1. 기둥이 한개 또는 0개 존재
zeros = array.count(0) 
if zeros == w or zeros == w-1:
    print(0)
    exit()

# 2. 기둥을 찾는 알고리즘 시작
p1, p2 = [], []
for i in range(w): # l->r, p1
    if i != w-1 and array[i] > array[i+1]:
        p1.append(i)
    if i == w-1: # 끝은 무조건 포함시키는게 예외의 케이스를 만들지 않는다.
        p1.append(i)
for i in range(w-1,-1,-1): # r->l, p2
    if i != 0 and array[i] > array[i-1]:
        p2.append(i)
    if i == 0:
        p2.append(i)
p = list(set(p1) & set(p2))

# 3. 기둥의 개수가 2개 이상이여야 계산이 가능
if len(p) < 2:
    print(0)
else: # 물이 담긴 양 계산한다.
    # zip 함수로 (좌,우) 기둥을 묶어준 다음 활용하자
    # 4 8, 3 1 2 3 4 1 1 2 -> 기둥이 3개 생기는 케이스
    water = 0
    for i, j in list(zip(p[:], p[1:])):
        height = min(array[i], array[j])
        for k in range(i+1, j):
            water += height - array[k]
    print(water)         
'''
    
# 2, 인터넷 답-투포인터를 응용한 방식
h, w = map(int, input().split())
array = list(map(int, input().split()))

l, r = 0, w-1
max_l, max_r = array[l], array[r]

water = 0

while l < r:
    max_l = max(max_l, array[l])
    max_r = max(max_r, array[r])
    if max_r >= max_l:
        water += max_l - array[l]
        l += 1
    else:
        water += max_r - array[r]
        r -= 1
print(water)
""" 210622 16:30 항해 30 QED """
# 풀이를 살펴보니 dequeue 라이브러리를 사용해서 쉽게 푸는것 같다.
import sys
inp = sys.stdin.readline
n, m = map(int, inp().split())

cQue = list()

for _ in range(n):
    cQue.append(_ + 1) # 1부터 N까지 삽입하기위해 1을 추가

def popNum():
    del cQue[0] # 0번에 항상 고정이므로 삭제시켜주기
    

def moveRight(Que):
    global cQue
    tempQue = Que[:]
    for i in range(n):
        tempQue[(i + 1) % n] = Que[i]
    cQue = tempQue
    return 

def moveLeft(Que):
    global cQue
    tempQue = Que[:]
    for i in range(n):
        tempQue[(i - 1) % n] = Que[i]
    cQue = tempQue
    return

# m만큼 출력하기
number_found = 0
counter = 0
target_nums = list(map(int, inp().split()))

while number_found < m:
    target_idx = cQue.index(target_nums[number_found]) # 목표값의 인덱스의 값을 cQue의 인덱스로 구하기
    # cur_idx와 목표값을 비교해서 더 짧은 이동거리 구하기
    if target_idx < n - target_idx:
        for i in range(target_idx):
            moveLeft(cQue)
            counter += 1
    else:
        for i in range(n-target_idx):
            moveRight(cQue)
            counter += 1
    popNum()
    n -= 1
    number_found += 1

print(counter)

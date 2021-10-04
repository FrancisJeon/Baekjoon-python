# 덱 210925
""" 
    push_front X: 정수 X를 덱의 앞에 넣는다.
    push_back X: 정수 X를 덱의 뒤에 넣는다.
    pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    size: 덱에 들어있는 정수의 개수를 출력한다.
    empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
    front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""
from collections import deque
from sys import stdin
input = stdin.readline

n = int(input())
deq = deque()

for _ in range(n):
    order = input().split()
    if order[0] == "push_front": deq.appendleft(order[1])
    elif order[0] == "push_back": deq.append(order[1])
    elif order[0] == "pop_front": print(deq.popleft()) if deq else print(-1)
    elif order[0] == "pop_back": print(deq.pop()) if deq else print(-1)
    elif order[0] == "size": print(len(deq))
    elif order[0] == "empty": print(0) if deq else print(1)
    elif order[0] == "front": print(deq[0]) if deq else print(-1)
    elif order[0] == "back": print(deq[-1]) if deq else print(-1)
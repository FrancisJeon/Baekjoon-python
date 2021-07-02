""" 210622 18:50 항해 31번 QED """
import sys
from collections import deque
inp = sys.stdin.readline

n = int(inp())
d = deque()

def push(order_lst):
    global d
    d.append(order_lst[1])

def pop():
    global d
    if not d:
        num = -1
    else:
        num = d.popleft()
    return num

def size():
    global d
    num = len(d)
    return num

def empty():
    global d
    if size() == 0:
        return 1
    else:
        return 0

def front():
    global d
    if empty():
        return -1
    else:
        return d[0]

def back():
    global d
    if empty():
        return -1
    else:
        return d[-1]

for _ in range(n):
    order = list(inp().split())
    if order[0] == 'push':
        push(order)
    elif order[0] == 'pop':
        print(pop())
    elif order[0] == 'size':
        print(size())
    elif order[0] == 'empty':
        print(empty())
    elif order[0] == 'front':
        print(front())
    elif order[0] == 'back':
        print(back())
    
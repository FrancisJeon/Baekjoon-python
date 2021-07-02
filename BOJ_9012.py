""" 210618 16:11 항해 23번 QED"""

import sys

t = int(sys.stdin.readline())

def isVps(sentence):
    stack = 0
    for i in range(len(sentence)):
        if sentence[i] == '(':
            stack += 1
        elif sentence[i] == ')':
            if stack <= 0:
                print('NO')
                return
            else:
                stack -= 1
    if stack != 0:
        print('NO')
    else:
        print('YES')

for _ in range(t):
    v = sys.stdin.readline()
    isVps(v)



""" 210621 01:00 항해 28번 QED """

import sys
hey = sys.stdin.readline

while True:
    stack = []
    isVPS = 1
    string = hey().rstrip()
    if string == '.':
        break
    for i in string:
        if not stack and i in [')', ']']:
            isVPS = 0
            break
        elif i in ['(', '[']:
            stack.append(i)
        elif i == ')':
            if stack[-1] == '(':
                del stack[-1]
            else:
                isVPS = 0
                break
        elif i == ']':
            if stack[-1] == '[':
                del stack[-1]
            else:
                isVPS = 0
                break
    print("yes" if isVPS and len(stack) == 0 else "no")


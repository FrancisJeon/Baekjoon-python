""" 210622 10:30 항해 29번 QED """
"""  
예제 입력 1 [8, 4 3 6 8 7 5 2 1]
예제 출력 1 [++++--++-++-----] 한줄로
예제 입력 2 [5, 1 2 5 3 4]
예제 출력 2 NO
"""
import sys
n = int(input())
inp = sys.stdin.readline
input_stack = []
order_stack = []
opr_stack = []

head_index = 0
for _ in range(n):
    nums = int(inp().rstrip())
    index_number = _ + 1 
    input_stack.append(nums)
    order_stack.append(index_number)
    opr_stack.append('+')

    while input_stack[head_index] == order_stack[-1]:
        opr_stack.append('-')
        del order_stack[-1]
        head_index += 1
        if not order_stack:
            break

if order_stack:
    print('NO')
else:
    for i in opr_stack:
        print(i)

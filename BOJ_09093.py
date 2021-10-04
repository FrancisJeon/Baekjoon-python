# 단어 뒤집기 210925
""" 
The input consists of T test cases. The number of test cases (T) is given in the first line of the input file. Each test case consists of a single line: each line contains a list of words separated by one space.

"""
import sys
input = sys.stdin.readline
# 1번 sys 로 입력하면 136ms 그냥 input()사용하면 880ms
""" n = int(input())
for _ in range(n):
    msg = list(input().split())
    new_msg = []
    for i in msg:
        this = i[::-1]
        new_msg.append(this)
    print(' '.join(new_msg)) """
# 2번 952ms, sys 160ms
n = int(input())
for _ in range(n):
    msg = list(input().split())
    for i in msg:
        print(i[::-1], end=' ')

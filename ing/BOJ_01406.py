# 에디터 211008
""" 
입력
처음 편집기에 입력된 문자열 (소문자로만 이뤄짐)
M 편집기에 넣을 명령어의 개수
명령들
출력
편집 후 문자열

* 알고리즘
커서는 맨 앞, 맨 뒤, 문장 중간에 위치할 수 있다.
처음 커서 위치는 문장의 맨 뒤
"""
# 너무 길고 지저분하다.
'''
import sys
input = sys.stdin.readline
n = input().rstrip()
c = len(n)  # 커서 위치
for _ in range(int(input())):
    order = list(map(str, input().rstrip().split()))
    
    if order[0] == 'L':
        c -= 1 if c != 0 else c   
    elif order[0] == 'D':
        c += 1 if c != len(n) else c
    elif order[0] == 'B':
        if c != 0:
            n = n[0:c-1] + n[c:]
            c -= 1
    elif order[0] == 'P':
        if c != 0:
            n = n[0:c] + order[1] + n[c:]
            c += 1
        else:
            n = order[1] + n
            c += 1
print(n)
'''

# 에디터 211008
""" 
입력
처음 편집기에 입력된 문자열 (소문자로만 이뤄짐)
M 편집기에 넣을 명령어의 개수
명령들
출력
편집 후 문자열

* 명령어
L = 커서 왼쪽으로 한칸, 맨 앞일땐 무시
D = 커서 우측으로 한칸, 맨 뒤이면 무시
B = 커서 왼쪽 문자 삭제, 맨앞이면 무시
P $ = $라는 문자를 커서 왼쪽에 추가

* 알고리즘
커서는 맨 앞 0, 맨 뒤 idx+1, 문장 중간에 위치할 수 있다.
처음 커서 위치는 문장의 맨 뒤
커서가 0일 때 글씨를 추가하면 맨 앞에 삽입되고 그 뒤의 인덱스들은 전부 +1

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

# 스택 두개를 활용해서 위치 옮겨주는 방식 -> 456ms
# 우측 스택은 값을 역순으로 뽑아줘야 정상출력 된다.
# stack1.extends(리스트[::-1]) -> 408ms
# .reverse() 함수 -> 440 ms
# order 자체를 문자열 자체보다 리스트로 받아서 인덱싱을 하는 케이스로 변경할 수 있지만 이건 테스트하지 않기로
import sys
input = sys.stdin.readline
left = list(input().rstrip())
right = []
for _ in range(int(input())): # 반복 횟수
    order = input().rstrip() 
    if order[0] == 'L':
        if left: right.append(left.pop())
    elif order[0] == 'D':
        if right: left.append(right.pop())
    elif order[0] == 'B':
        if left: left.pop()
    elif order[0] == 'P':
        word = order.split()[1]
        left.append(word)

# print(f"{''.join(left)}{''.join(right[::-1])}")

# left.extend(right[::-1])
# print(''.join(left))

right.reverse()
print(''.join(left + right))
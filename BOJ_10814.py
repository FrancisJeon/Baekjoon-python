# 나이순 정렬 211001
""" 
n명의 회원이 주어지고
나이와 이름이 공백으로 주어진다.
나이 오름차순, 나이가 같으면 '가입한 순'으로

# 저장할 때 가입순서 담기
문제는 input은 전부 문자열이라서 sorting에서 문제가 살짝 발생한다.
"""
# 1차 코드
# import sys
# input = sys.stdin.readline
# member = [list(map(str, input().split()))+[_] for _ in range(int(input()))]
# for age, name, order in sorted(member, key = lambda x: (int(x[0]),x[2])): # x[2]가 가입한 순
#     print(age, name)

# 답안코드 보니까 list(map(str, input().split())) 없이도 리스트 형태로 담아줄 수 있나보다.
import sys
input = sys.stdin.readline
member = [input().split() + [_] for _ in range(int(input()))]
for age, name, order in sorted(member, key=lambda x: (int(x[0]), x[2])):
    print(age, name)

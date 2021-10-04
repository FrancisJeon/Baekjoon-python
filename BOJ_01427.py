# 소트인사이드 211001
""" 
입력된 숫자를 내림차순으로 바꾸어서 출력
1234 -> 4321
14359 -> 95431
print(sorted(input()))
sorted 자체가 리스트를 반환하기 때문에 list(input()) 할 필요가 없다.
"""
# print(''.join(sorted(list(input()),reverse=True)))
print(''.join(sorted(input())[::-1]))
# print(*sorted(input())[::-1],sep='')
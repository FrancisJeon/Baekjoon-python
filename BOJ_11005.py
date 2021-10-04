# 진법 변환2 210927
""" 
10진법 수 N이 주어지면 B진법으로 바꾸기
"""
n, b = map(str, input().split())
b = int(b)
# 10진법 수를 B진법으로 계속 나눈 값들을 사용해야 할듯
result = 0
for i in n[::-1]: # 문자열을 역으로 돌면서 해당 문자열의 숫자를 int형태로 변경해준 뒤 temp 값을 진법만큼 배수로 바꿔서 다음 값을 계산한다
    if '0' <= i <= '9':
        a = ord(i) - ord('0')
    else:
        a = ord(i) - ord('A') + 10
    a *= temp
    result += a
    temp *= b

print(result)
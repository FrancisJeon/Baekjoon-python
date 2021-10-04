# 진법 변환 210927
""" 
B진법 수 N이 주어지면 10진법으로 바꾸기
"""
# N, B = map(str, input().split())
# print(int(N, int(B)))

# 진법 자동변환 쓰지 않은 풀이
n, b = map(str, input().split())
b = int(b)
temp = 1
result = 0
for i in n[::-1]:  # 문자열을 역으로 돌면서 해당 문자열의 숫자를 int형태로 변경해준 뒤 temp 값을 진법만큼 배수로 바꿔서 다음 값을 계산한다
    if '0' <= i <= '9':
        a = ord(i) - ord('0')
    else:
        a = ord(i) - ord('A') + 10
    a *= temp
    result += a
    temp *= b

print(result)

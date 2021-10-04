# 카이사르 암호 210922
n = input()
answer = [chr( (ord(i) - ord('D')) % 26 + ord('A') ) for i in n]
ans = ''.join(answer)
print(ans)

# 1차 정답
# for i in n:
#     ord(i) % 25 + 65
#     if ord(i) < 68:
#         ans += chr(ord(i) + 23)
#     else:
#         ans += chr(ord(i) - 3)
# print(ans)

# 어떤 값이 나와야 하는데 
# ABC 3 값의 경우 XYZ가 나오고 나머지 경우엔 아스키코드 -3 값이 나오게 해야한다..
# ord(i) - ord('A') 하면 전부 0부터 25가 나오는데 이 상태로 -3을 한 뒤 % 25 + 65 하기?
# 26으로 나눴어야 하는데 25로 나눠서 오답이다.. 근데 0~25 사이를 내려면 25로 나누는게 맞지않나 -로 가서 그런가

# 알파벳 찾기 210924
# 1차 76ms
s = input()
s = list(s.upper())
alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
lst = [-1] * 26

for i in range(len(s)):
    if lst[alphabet.index(s[i])] == -1:
        lst[alphabet.index(s[i])] = i
for j in lst:
    print(j, end=' ')
    
# 2차 104ms
S = input()
list_alpha = [-1] * 26 # a~z까지의 첫 등장 위치 담는 리스트
for i, w in enumerate(S):
    # baekjoon의 경우 b의 인덱스 0, 단어 b
    if list_alpha[ord(w) - ord('a')] == -1:
        list_alpha[ord(w) - ord('a')] = i
for i in list_alpha:
    print(i, end= ' ')

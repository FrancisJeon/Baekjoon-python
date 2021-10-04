# 평균 210924
# 자기 점수 중 최댓값을 M으로 잡고 모든 점수를 점수/M * 100으로 고쳤다.
# 새로운 평균 구하는 프로그램

# 2차
n = int(input())
scores = list(map(int, input().split()))
def new_score(array):
    new_arr = []
    M = max(array)
    for i in array:
        new_arr.append(i/M * 100)
    return new_arr
print(sum(new_score(scores))/n)

# 3차
n = int(input()); scores = list(map(int, input().split()))
M = max(scores); score = 0
for i in scores:
    score += i/M * 100
print(score/n)
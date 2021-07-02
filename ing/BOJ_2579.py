""" 210616 16:00 항해 37번 by 신영"""
"""
계단 오르기 게임은 계단 아래 시작점부터 계단 꼭대기에 위치한 도착점까지 가는 게임이다. 각각의 계단에는 일정한 점수가 쓰여 있는데 계단을 밟으면 그 계단에 쓰여 있는 점수를 얻게 된다.
계단 오르는 데는 다음과 같은 규칙이 있다.
계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
마지막 도착 계단은 반드시 밟아야 한다.
이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하시오.
입력
입력의 첫째 줄에 계단의 개수가 주어진다.
둘째 줄부터 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수가 주어진다. 계단의 개수는 300이하의 자연수이고, 계단에 쓰여 있는 점수는 10, 000이하의 자연수이다.
출력
첫째 줄에 계단 오르기 게임에서 얻을 수 있는 총 점수의 최댓값을 출력한다.
입력 
6
10
20
15
25
10
20
출력 75
"""
# from sys import stdin
# stairs = int(stdin.readline())

# for _ in range(stairs):
    # score = int(stdin.readline())
    # scoreLst.append(score)

stairs = 6
scoreLst = [10, 20, 15, 25, 10, 20]
scoreLst.reverse()
# scoreLst.append(0)

v1Score = 20
v2Score = 20
indexV1 = 1
indexV2 = 2

while indexV1 <= len(scoreLst):
    v1Score += scoreLst[indexV1]
    indexV1 += 2
    if indexV1 >= len(scoreLst):
        break
    v1Score += scoreLst[indexV1]
    indexV1 += 1

while indexV2 <= len(scoreLst):
    v2Score += scoreLst[indexV2]
    indexV2 += 1
    if indexV1 >= len(scoreLst):
        break
    v2Score += scoreLst[indexV2]
    indexV2 += 2

print(max(v1Score, v2Score))

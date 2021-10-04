# 홀수 210924 
# 7개의 자연수가 주어지면 그 중 홀수만 골라 합을 구하고 홀수 중 최솟값 찾는 프로그램
# 만약 홀수 없으면 -1 출력

odds = [int(input()) for i in range(7)]
sort_odds = sorted(list(filter(lambda x: x % 2, odds)))
print(sum(sort_odds), sort_odds[0]) if sort_odds else print(-1)

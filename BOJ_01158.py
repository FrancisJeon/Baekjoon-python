""" 210703 요세푸스 문제 """
"""
1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를(N, K)-요세푸스 순열이라고 한다. 예를 들어(7, 3)-요세푸스 순열은 < 3, 6, 2, 7, 5, 1, 4 > 이다.
N과 K가 주어지면(N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.
입력
첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 5, 000)
출력
예제와 같이 요세푸스 순열을 출력한다.
예제 입력 1 => 7 3
죽은 순서 -> 3 6 2 7 5 1 4 -> 죽으면 0으로 만들어서 0일경우 다음사람 죽이는 방법?

"""
# 1 2 3 4 5 6 7 / 2번인덱스 삭제 후 4번인덱스 갔다가 다시 앞으로 돌아가는데 기준은 len(people)
'''
def josephus_problem(n, k):
    result_arr = []

    next_index = k - 1
    people_arr = list(range(1, n + 1))

    while people_arr:
        print(next_index)
        result = people_arr.pop(next_index)
        result_arr.append(result)
        if len(people_arr) != 0:
            next_index = (next_index + (k - 1)) % len(people_arr)

    print("<", ", ".join(map(str, result_arr)), ">", sep='')
'''
from collections import deque

n, k = map(int, input().split()) # n 사람 수 k 간격
ppl = deque([_+1 for _ in range(n)]) # 1~n 까지의 사람들을 담아둠
answer = []
while len(answer) != n:
    ppl.rotate(-k)
    answer.append(ppl.pop())
print(f"<{', '.join(map(str, answer))}>")

# while len(ans) != n:
#     idx += k
#     if ppl[idx] != 0:
#         ans.append(ppl[idx])
#         ppl[idx] = 0
#     elif ppl[idx] == 0:
#         idx += 1
    
    

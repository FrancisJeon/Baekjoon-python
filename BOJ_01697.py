# 숨바꼭질 210926
""" 
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

동생의 위치는 고정이고 수빈이가 한번에 움직일 수 있는거리가 +1, -1, 2X 위치라고 가정하면 가장 빠르게 동생의 위치로 이동하는 시간 구하기

1: [x-1, x+1, 2x]
2: 1번값-1, 1번값+1, 1번값*2
이런식으로 계속 늘리면서 k가 존재하는 순간의 값을 반환해보자
리스트 내부의 값을 반복문을 활용해서 +1 한 값들의 리스트와 -1 한 값들의 리스트 *2 한 값들의 리스트를 담아서 하나의 리스트로 옮기기? 아니면 0~10만까지의 키에 도달하는 시간을 리스트로 만들어서 담아두기? 그래서 dict[k]가 존재하는 순간이 정답?
"""
# 메모리 초과가 나온다. -> set로 변경 = 시간초과
# n, k = map(int, input().split()) # n 은 시작위치 k 는 종료위치라고 생각하기
# path_dict = {0:set([n])}
# time = 0

# while k not in path_dict[time]:
#     for i in path_dict[time]:
#         if path_dict.get(time+1) == None:
#             path_dict[time+1] = set([i + 1]); 
#             if i == 0:
#                 continue
#             path_dict[time+1] = path_dict[time+1] | set([i - 1]); 
#             path_dict[time+1] = path_dict[time+1] | set([i * 2])
#         else:  # 처음 값이 없을 때는 = 으로 삽입이 되는데 += 을 안해주면서 다시 초기화로 사라진다..
#             path_dict[time+1] = path_dict[time+1] | set([i + 1])
#             if i == 0:
#                 continue
#             path_dict[time+1] = path_dict[time+1] | set([i - 1])
#             path_dict[time+1] = path_dict[time+1] | set([i * 2])
#     if k in path_dict[time]: break
#     time += 1
# print(time)


# 메모리 초과를 방지하기 위해 visited = [0] * 10000001 에서 들르는 순간 time을 기록하고 이미 visited면 들리지 않는 방법을 사용해보겠음
# deque를 같이 사용해줘서 [위치, 시간]을 기록하자
from collections import deque

def bfs(v):
    count = 0 # 시간
    q = deque([[v, count]]) # 시작점, 시간을 큐에 넣어준 다음 pop 하면서 빌 때 까지 반복 만약 뽑아서 나온 n이 정답과 일치하는 순간 그 시간을 정답으로 출력한다. 
    # 왜 2차원을 사용했는가? 그래야 출력할 때 1차원으로 출력된다. 아닌 경우 5, 0 이렇게 따로 출력되버림
    while q:
        v = q.popleft()
        e = v[0]
        count = v[1]
        if not visited[e]: # 만약 이번 값이 방문하지 않은 곳이라면
            visited[e] = True
            if e == k:
                return count
            count += 1 # 시간은 하나 늘린 다음 e에 + - * 해준 값들을 큐로 넣어준다?
            if e * 2 <= 100000:
                q.append([e*2, count])
            if e + 1 <= 100000:
                q.append([e+1, count])
            if e - 1 >= 0:
                q.append([e-1, count])
    return count


n, k = map(int, input().split())
visited = [False] * 100001
print(bfs(n))
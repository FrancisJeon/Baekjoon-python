# 멀티탭 스케쥴링 211001
""" 
N개의 멀티탭 구멍에 K개의 최대 사용횟수가 주어진다.
전기용품의 이름이 K 이하의 자연수로 사용
플러그를 빼는 최소의 횟수를 출력한다. 

입력 
2 7
2 3 2 3 1 2 7

2 와 3을 꽂고 있다가 *3을 빼고* 1을 꽂은 뒤 *1을 빼고* 7을 꽂으면 전부 다 꽂을 수 있다. -> 2번
# set 형태로 전부 삭제시킨 다음에 입력값 n에서 빼주면 횟수가 나오려나 X
# 대신 맨앞에 두번은 플러그에 무조건 삽입해야 한다.
* 알고리즘
멀티탭이 비어있다면 멀티탭을 채운다.
멀티탭에 이미 들어가 있는 아이템이 나온다면 continue로 다음 인덱스로 넘어간다.
멀티탭이 꽉 찬 상태에서 새로운 아이템 나온다면 


"""

from collections import defaultdict, deque
import sys


if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    array = list(map(int, sys.stdin.readline().split()))

    # 전기 용품의 종류에 따른 인덱스 저장 딕셔너리 (name_dict)
    name_dict = defaultdict(deque)
    for i in range(len(array)):
        name_dict[array[i]].append(i)
    print(name_dict)
    # 멀티탭 구멍의 개수만큼 큐에 삽입
    q = deque()
    cnt = 0
    index = 0
    while cnt < n: # q의 갯수가 cnt이고 이게 n개가 되면 이 반복문을 빠져나감
        if array[index] not in q:
            q.append(array[index])  # 삽입, 0번째 인덱스부터 순서대로 while 문 돌려줌
            name_dict[array[index]].popleft()  # 인덱스 삭제
            cnt += 1
        else:
            name_dict[array[index]].popleft()
        index += 1

    # 현재 멀티탭에 꽂아진 전기용품 중 가장 뒤늦게 다시 등장하는 전기용품 찾아서 바꾼다
    answer = 0
    result = set()
    for i in range(index, k): # index가 q가 다 찰때까지 진행한 상태로 멈춰있었으니까 거기부터 시작
        print(f"current index = {i}")
        if array[i] in q:  # 이미 꽂혀있는 경우
            name_dict[array[i]].popleft()
            continue
        else:
            index, value = -1, None # 역순의 index와 value
            for j in range(n):
                if len(name_dict[q[j]]) == 0: # namedict 내부에 q의 j번째 값이 길이가 0인 경우 (더 사용하지 않을 경우?) break -> i번째 인덱스..?
                    index, value = -1, q[j]
                    break
                if index < name_dict[q[j]][0]: # 인덱스가 더 작다는건 무슨 의미지, 딕셔너리에 [0]번째는 해당 값의
                    index, value = name_dict[q[j]][0], q[j]
            answer += 1
            q.remove(value)
            q.append(array[i])
            if len(name_dict[array[i]]) != 0:
                name_dict[array[i]].popleft()

    print(answer)

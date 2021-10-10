# 부분합 211004
"""
1만 이하의 자연수로 이루어진 N길이의 수열이 주어질 때 
연속된 수열의 부분합 중 S 이상이 되는 가장 짧은것의 길이 구해라
합을 만드는게 불가능 하다면 0을 출력

입력
N S (N 길이, S 최솟값)
N 길이의 수열

알고리즘
start, end를 포인터로 잡고 왼쪽부터 하나씩 우측으로 늘리면서 S보다 작을 때는 end를 늘리고 S보다 길어지면 start를 늘린다.
모든 S 초과의 경우의 길이를 답지에 담을 때 min으로 비교해서 넣기

문제점 1 - start가 s를 포함하는 경우 가장 짧은건 1이 나오긴 하는데 start만 끝까지 늘어나고 end는 늘어나지 않는다. -> s,e를 둘다 늘리는 걸로 해결

* s,e를 둘다 0으로 잡고 0:0을 해주면 sum은 무조건 0이 나온다. -> sum은 사용하지 못하게 되었다.
* ### s는 항상 e보다 작거나 같게끔 함수를 짜야한다.
* ### 반복문의 종료 조건은 end가 끝보다 작거나 같을 때 -> True로 end == n이 되는 조건을 탈출문으로 바꿔보았다.

* 3항 연산 부분을 +=와 함께 사용하고 싶다. 성공한 듯? 한데 좀 더 살펴봐야겟다 
## 삼항 연산자 만들어 봤는데 이 방법은 안될 것 같다.
if start < end:
    start += 1
else:
    start += 1; end += 1 # 둘이 같을 경우인데 (더 큰 케이스는 안나오게 막았으니까) 둘 다 하나씩 옮겨준 상태로 while문 돌리기 
start = start + 1 if start < end else (start + 1 and end + 1) # 로 만들어 보았다. 근데 생각해보면 start +1 end +1은 연산이지 결과를 저장하진 않을 것 같다.



### 첫 제출 시간초과 뜸 -> sum 함수를 반복하는게 문제라면 부분합을 이용한 array를 만들어 봐야겠다.
### 두번째 제출은 부분합을 직접 만들어가면서 제작했는데 오답이 나왔다.
# end와 길이가 같아질 때 제대로 탈출을 못해줘서 index 에러가 발생한다.

### 답지 코드는 첫 코드랑 큰 차이가 없는데 right == end 조건을 탈출문으로 사용하는것 하나로 코드가 많이 깔끔해졌다.
"""
# 정답, 코드가 길어서 줄여줄 생각
# import sys
# input = sys.stdin.readline

# n,s = map(int, input().split())
# array = list(map(int, input().split()))

# start, end = 0, 0
# ans = 9999999
# partial_sum = sum(array[start:end]) 
# # end라고 해도 0번째 값을 담아둔다면 시작부터 partial sum은 sum[0:1]으로 시작하는 것과 같다.
# # 순서를 바꿔서 처음에 end+=1 연산 전에 partial sum으로 바꿔보았다. 이러면 좀 힘들것 같다.. 처음에만 sum 함수 사용해보았다.
# while end <= n: 
#     # end보다 짧거나 같을 때까지 늘려준다. sum 이 아닐 때는 도달하면 탈출시켜야 한다.
#     if partial_sum >= s:
#         ans = min(ans, end-start) 
#         # sum 함수를 안쓰면 end-start+1을 적어줘야 하나보다, 방식을 변경했기 때문에 end-start로 해봤음
#         if ans == 1:
#             print(1)
#             exit()
#         # 만약 1줄에 모든게 다 담긴 숫자가 나오면 바로 탈출해서 1 출력하고 exit() 시키자
#         partial_sum -= array[start]
#         # 이렇게 측정을 했다면 start 위치를 우측으로 하나 옮겨주기 위해 그 값을 부분합에서 제거했다.
#         start += 1

#     elif partial_sum < s:
#         # end가 탈출하는 조건을 한번 더 달아야겠다.
#         if end == n:
#             break
#         partial_sum += array[end] 
#         # 0번 인덱스 값이 더해지면서 end값이 하나 증가 -> 4일 때 partial_sum 검사하면 14였으니까 한번 증가 후 0:5 일때 sum은 24고 길이는 5가 나와야 한다.
#         end += 1
# print(ans if ans != 9999999 else 0)

# 코드 단축
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
array = list(map(int, input().split()))

start, end, ans, partial_sum = 0, 0, 1e9, 0
while True:
    if partial_sum >= s:
        ans = min(ans, end-start)
        partial_sum -= array[start]; start += 1
        if ans == 1: print(1); exit()
    elif end == n: break
    else: partial_sum += array[end]; end += 1
print(ans if ans != 1e9 else 0)

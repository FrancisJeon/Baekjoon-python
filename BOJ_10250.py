""" 210617 12:06 항해 17번 QED AMC 호텔"""
# 호텔은 W개의 방이 있는 H층 건물
# 방 번호는 YXX 나 YYXX 형태인데 여기서 Y 나 YY 는 층 수를 나타내고 XX 는 엘리베이터에서부터 세었을 때의 번호를 나타낸다.

# 101부터 시작 h01호가 차면 102:h02 103:h03 ....10w:h0w
# h 변할 수 있다. w도 변할 수 있다. n은 만들어진 방의 순서에서 n번째에 해당하는 방
# 출력결과는 배정될 방번호

t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    # h층 w호 n손님 번호 
    rooms = ['000'] # 0번 인덱스를 채워줌
    for i in range(1, w+1):
        for j in range(1, h+1):
            rooms.append(f'{j}{str(i).zfill(2)}')

    print(rooms[n])



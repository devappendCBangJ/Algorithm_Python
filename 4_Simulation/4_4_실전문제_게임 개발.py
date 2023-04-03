# input 받아오기
map_size = input().split()
coor = input().split()
map = []
w, h = int(map_size[0]), int(map_size[1])
x, y, dir = int(coor[0]), int(coor[1]), int(coor[2])
for _ in range(h):
    map.append(input().split())
# print(w, h, x, y ,dir)
# print(map)

# 변수 정의
visit_count = 0
rotate_count = 0
dir_change = {'0':'1', '1':'2', '2':'3', '3':'0'}
dir_move = {'0':'12', '1':'01', '2':'10', '3':'21'} # 북 : y방향 + 1 / 서 : x방향 - 1 / 남 : y방향 - 1 / 동 : x방향 + 1

while(True):
    # 4방향 전부 회전 : 가보지 않은 곳 방문
    while(rotate_count <= 3):
        dir = int(dir_change[str(dir)])
        rotate_count += 1
        dxdy = dir_move[str(dir)]
        dx, dy = int(dxdy[0])-1, int(dxdy[1])-1
        # 가보지 않은 곳 : 기존 좌표는 방문 표시 + 다음 좌표 방문

        if x+dx < 0 or x+dx >= w or y+dy < 0 or y+dy >= h:
            continue
        if map[x+dx][y+dy] == '0':
            # 현재 좌표가 안가본 곳 : visit 추가
            if map[x][y] == '0':
                map[x][y] = '2'
                visit_count += 1
            x, y = x+dx, y+dy
            go_back = False
            break
    # 4방향 전부 갈 곳 없음 : 뒤가 바다가 아니면, 뒤로 가기
    if go_back == True:
        dxdy = dir_move[str(dir)]
        dx, dy = -(int(dxdy[0])-1), -(int(dxdy[1])-1)
        if x+dx < 0 or x+dx >= w or y+dy < 0 or y+dy >= h:
            continue
        if map[x+dx][y+dy] == '2':
            # 현재 좌표가 안가본 곳 : visit 추가
            if map[x][y] == '0':
                map[x][y] = '2'
                visit_count += 1
            x, y = x+dx, y+dy
        elif map[x+dx][y+dy] == '1':
            break
    go_back = True
    rotate_count = 0
    # print(map)

print(visit_count)
# ---------------------------------------------------
# 나의 풀이 -> 실패
# ---------------------------------------------------
"""
from collections import deque

rectangle = []
board = [[0 for _ in range(10)] for _ in range(10)]
rec_board = [[[] for _ in range(10)] for _ in range(10)]

rec_num = int(input())
for _ in range(rec_num):
    rectangle.append(list(map(int, input().split())))

characterX, characterY, itemX, itemY = list(map(int, input().split()))

for b in board:
    print(b)
for rb in rec_board:
    print(rb)
print(rectangle, characterX, characterY, itemX, itemY)

for idx, r in enumerate(rectangle):
    for x in range(r[0], r[2]+1):
        board[r[1]][x] += 1
        board[r[3]][x] += 1
        rec_board[r[1]][x].append(idx)
        rec_board[r[3]][x].append(idx)
    for y in range(r[1]+1, r[3]):
        board[y][r[0]] += 1
        board[y][r[2]] += 1
        rec_board[y][r[0]].append(idx)
        rec_board[y][r[2]].append(idx)

    if min(abs(r[0] - r[2]), abs(r[1] - r[3])) > 1:
        for y in range(r[1] + 1, r[3]):
            for x in range(r[0] + 1, r[2]):
                board[y][x] += 3
    # break

for b in board:
    print(b)
for rb in rec_board:
    print(rb)

queue = deque([[characterX, characterY]])
while queue:
    x, y = queue.popleft()
    board[y][x] = 1000

    for nx, ny in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
        if board[ny][nx] >= 3:
            break
"""

# ---------------------------------------------------
# 나의 풀이 -> 다른 사람 풀이 보고, 좌표계 2배 BFS 풀이 성공 -> 여기서는 작동잘됨
# ---------------------------------------------------
"""
from collections import deque

board = [[0 for _ in range(20)] for _ in range(20)]
track_board = [[-1 for _ in range(20)] for _ in range(20)]

rectangle = []
rec_num = int(input())
for _ in range(rec_num):
    rectangle.append(list(map(lambda x: 2 * int(x), input().split())))

characterX, characterY, itemX, itemY = list(map(lambda x: 2 * int(x), input().split()))

# for b in board:
#     print(b)
# print(rectangle, characterX, characterY, itemX, itemY)

for idx, r in enumerate(rectangle):
    for x in range(r[0], r[2] + 1):
        board[r[1]][x] += 1
        board[r[3]][x] += 1
    for y in range(r[1] + 1, r[3]):
        board[y][r[0]] += 1
        board[y][r[2]] += 1

    for y in range(r[1] + 1, r[3]):
        for x in range(r[0] + 1, r[2]):
            board[y][x] += 3
    # break

# for b in board:
#     print(b)

queue = deque([[characterX, characterY]])
track_board[characterY][characterX] = 0
while queue:
    x, y = queue.popleft()

    for nx, ny in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
        if nx < 0 or nx >= 20 or ny < 0 or ny >= 20:
            continue
        elif board[ny][nx] >= 3 or board[ny][nx] <= 0:
            continue
        elif track_board[ny][nx] >= 0:
            continue
        else:
            queue.append([nx, ny])
            track_board[ny][nx] = track_board[y][x] + 1
            # print(track_board)

            if nx == itemX and ny == itemY:
                print(track_board[ny][nx] // 2)
    # print(queue)
"""

# ---------------------------------------------------
# 나의 풀이 -> 다른 사람 풀이 보고, 좌표계 2배 BFS 풀이 성공 -> 프로그래머스에서 작동 잘됨
# ---------------------------------------------------
from collections import deque

board = [[0 for _ in range(101)] for _ in range(101)] # 여기 101이 아니라 100으로 하면 왜 안되지???
track_board = [[-1 for _ in range(101)] for _ in range(101)]

def solution(rectangle, characterX, characterY, itemX, itemY):
    characterX, characterY = 2 * characterX, 2 * characterY
    itemX, itemY = 2 * itemX, 2 * itemY

    for idx, r in enumerate(rectangle):
        r = list(map(lambda x: 2 * x, r))
        for x in range(r[0], r[2] + 1):
            board[r[1]][x] += 1
            board[r[3]][x] += 1
        for y in range(r[1] + 1, r[3]):
            board[y][r[0]] += 1
            board[y][r[2]] += 1

        for y in range(r[1] + 1, r[3]):
            for x in range(r[0] + 1, r[2]):
                board[y][x] += 3

    queue = deque([[characterX, characterY]])
    track_board[characterY][characterX] = 0
    while queue:
        x, y = queue.popleft()

        for nx, ny in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
            if nx < 0 or nx >= 101 or ny < 0 or ny >= 101:
                continue
            elif board[ny][nx] >= 3 or board[ny][nx] <= 0:
                continue
            elif track_board[ny][nx] >= 0:
                continue
            else:
                queue.append([nx, ny])
                track_board[ny][nx] = track_board[y][x] + 1

                if nx == itemX and ny == itemY:
                    return track_board[ny][nx] // 2
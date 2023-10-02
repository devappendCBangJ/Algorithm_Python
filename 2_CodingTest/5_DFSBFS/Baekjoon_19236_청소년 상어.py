# 240min 오답

from collections import deque
from copy import deepcopy

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

shark_coor = [0, 0]
fishes_coor = [0 for _ in range(16)]
dir_board = [[0 for _ in range(4)] for _ in range(4)]
idx_board = [[16 for _ in range(4)] for _ in range(4)]
result = 0
score = 0
for r in range(4):
    line = list(map(int, input().split()))
    for c in range(4):
        dir_board[r][c] = line[c*2+1] - 1
        idx_board[r][c] = line[c*2] - 1
        fishes_coor[line[c*2] - 1] = [r, c]
# print(fishes_coor)

dir_board[0][0] += 10 # 상어라는 것을 구분하기 위해 +10!!!
score += (idx_board[0][0] + 1) # 초기에 상어가 물고기 먹을 때의 score 지정해줘야함!!!
# print(dir_board)
queue = deque([[shark_coor, fishes_coor, dir_board, idx_board, score]])
# idx_board[0][0] = 16 # 굳이 없어도 됨
while queue:
    shark_coor, fishes_coor, dir_board ,idx_board, score = queue.popleft()
    # print(dir_board)
    # 모든 물고기 이동
    for i, (fr, fc) in enumerate(fishes_coor):
        if 0 <= dir_board[fr][fc] <= 7: # 물고기가 해당 위치에 있는 경우만 연산!!!
            # print(fr, fc, dir_board[fr][fc])
            # 다음 칸 빈칸 : 위치, 방향, 인덱스 Swap
            nr = fr + dr[dir_board[fr][fc]]
            nc = fc + dc[dir_board[fr][fc]]
            if (0 <= nr < 4 and 0 <= nc < 4) and dir_board[nr][nc] == 9:
                # print(fr, fc, dir_board[fr][fc])
                fishes_coor[i] = [nr, nc]
                dir_board[nr][nc], dir_board[fr][fc] = dir_board[fr][fc], dir_board[nr][nc]
                idx_board[nr][nc], idx_board[fr][fc] = idx_board[fr][fc], idx_board[nr][nc]
            else:
                # 다음 칸 상어 or 벽 : 방향 45도 반시계 회전
                rot_i = 1
                while (nr < 0 or 4 <= nr or nc < 0 or 4 <= nc) or 10 <= dir_board[nr][nc]:
                    if rot_i <= 8:
                        dir_board[fr][fc] = (dir_board[fr][fc] + 1) % 8 # 방향을 바꾼 것을 적용해줘야함!!!
                        nr = fr + dr[dir_board[fr][fc]]
                        nc = fc + dc[dir_board[fr][fc]]
                        rot_i += 1
                    else: # rot_i가 8보다 같거나 큰 경우를 추가 안해주면 break 못하고 무제한으로 돌 수 있음!!!
                        break
                # 다음 칸 다른 물고기 있음 : 위치, 방향, 인덱스 Swap
                if (0 <= nr < 4 and 0 <= nc < 4) and 0 <= dir_board[nr][nc] <= 7:
                    # print(dir_board[nr][nc])
                    fishes_coor[i], fishes_coor[idx_board[nr][nc]] = [nr, nc], [fr, fc]
                    idx_board[nr][nc], idx_board[fr][fc] = idx_board[fr][fc], idx_board[nr][nc]
                    dir_board[nr][nc], dir_board[fr][fc] = dir_board[fr][fc], dir_board[nr][nc]
        # print(idx_board)
    # 상어 움직임
    sr, sc = shark_coor
    dir_s = dir_board[sr][sc] - 10 # 상어라는 것을 구분하기 위해 +10 해뒀던 것을 빼줌!!!
    # print(sr, sc, dir_s)
    for length in range(1, 4):
        nr = sr + dr[dir_s] * length
        nc = sc + dc[dir_s] * length
        if (0 <= nr < 4 and 0 <= nc < 4) and 0 <= dir_board[nr][nc] <= 7:
            fishes_coor[i], fishes_coor[idx_board[nr][nc]] = [nr, nc], [fr, fc] # fishes_coor 위치도 바꿔줘야함!!!
            # print(fishes_coor[i], fishes_coor[idx_board[nr][nc]], [nr, nc], [fr, fc])
            dir_board[sr][sc] = 9
            dir_board[nr][nc] += 10 # 상어라는 것을 구분하기 위해 +10!!!
            # idx_board[nr][nc] = 16 # 굳이 없어도 됨
            shark_coor = [nr, nc]
            result = max(result, score + idx_board[nr][nc] + 1) # index를 배열로 mapping하기 위해서 -1 했었으니까, score 계산할 때는 +1해서 다시 되돌려줌!!!
            # print("dir : ", dir_board)
            # print("idx : ", idx_board)
            # print("score : ", score, idx_board[nr][nc] + 1) # index를 배열로 mapping하기 위해서 -1 했었으니까, score 계산할 때는 +1해서 다시 되돌려줌!!!
            queue.append([shark_coor[:], fishes_coor[:], deepcopy(dir_board), deepcopy(idx_board), score + idx_board[nr][nc] + 1]) # deepcopy하지 않으면 참조로 들어가서 queue안에 있는 배열 값이 함께 바뀌어버림!!!
            fishes_coor[i], fishes_coor[idx_board[nr][nc]] = [fr, fc], [nr, nc]
            dir_board[nr][nc] -= 10 # 다음 for문을 돌기 위해 +10 해뒀던 것을 빼줌!!!
    # for q in queue:
    #     print(q)
print(result)


"""
# ---------------------------------------------------
# 다른 사람 풀이 -> bfs 깊어지면서 idx_board 배열 저장에 많은 메모리가 필요한데, 2중 for문으로 그때 그때 찾아내는 방식으로 시간 복잡도를 희생하는 대신 메모리를 아낌
# https://developer-ellen.tistory.com/68
# ---------------------------------------------------
# DFS+구현
import copy

board = [[] for _ in range(4)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    data = list(map(int, input().split()))
    fish = []
    for j in range(4):
        # 물고기 번호, 방향
        fish.append([data[2*j], data[2*j+1]-1])
    board[i] = fish

max_score = 0

def dfs(sx, sy, score, board):
    global max_score
    score += board[sx][sy][0]
    max_score = max(max_score, score)
    board[sx][sy][0] = 0

    # 물고기 움직임
    for f in range(1, 17):
        f_x, f_y = -1, -1
        for x in range(4):
            for y in range(4):
                if board[x][y][0] == f:
                    f_x, f_y = x, y
                    break
        if f_x == -1 and f_y == -1:
            continue
        f_d = board[f_x][f_y][1]

        for i in range(8):
            nd = (f_d+i) % 8
            nx = f_x + dx[nd]
            ny = f_y + dy[nd]
            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == sx and ny == sy): # if문을 만족하지 않으면 아래 코드가 실행되지 않게끔 만들어둠!!!
                continue
            board[f_x][f_y][1] = nd
            board[f_x][f_y], board[nx][ny] = board[nx][ny], board[f_x][f_y]
            break

    # 상어 먹음
    s_d = board[sx][sy][1]
    for i in range(1, 5):
        nx = sx + dx[s_d]*i
        ny = sy + dy[s_d]*i
        if (0 <= nx < 4 and 0 <= ny < 4) and board[nx][ny][0] > 0:
            dfs(nx, ny, score, copy.deepcopy(board))

dfs(0, 0, 0, board)
print(max_score)
"""
# 120min 소요

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

# 토네이도 이동 경로
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
pos_list = [[0, 0]]
pos = [0, 0]
dir = 0
move_board = [[0 for _ in range(N)] for _ in range(N)]
move_board[0][0] = 1
while pos != [N//2, N//2]:
    nr = pos[0] + dr[dir]
    nc = pos[1] + dc[dir]
    if not (0 <= nr <= N-1 and 0 <= nc <= N-1) or move_board[nr][nc] != 0:
        dir = (dir + 1) % 4
        continue
    move_board[nr][nc] = 1
    pos = [nr, nc]
    pos_list.append(pos)
# print(pos_list)

# 토네이도 이동 + 모래 흩날리기
total_result = 0
for i in range(len(pos_list)-2, -1, -1):
    r, c = pos_list[i]
    mr = r - pos_list[i+1][0]
    mc = c - pos_list[i+1][1]
    remain_sand = board[r][c]

    # 대각선 방향
    if mr == 0:
        next_list = [[1, mc, 0.10], [-1, mc, 0.10], [1, -mc, 0.01], [-1, -mc, 0.01]] # 방향 정의 실수 주의!!!
    else:
        next_list = [[mr, 1, 0.10], [mr, -1, 0.10], [-mr, 1, 0.01], [-mr, -1, 0.01]]
    for dr, dc, ratio in next_list:
        nr = r + dr
        nc = c + dc
        small_sand = int(board[r][c] * ratio)
        remain_sand -= small_sand
        if 0 <= nr <= N - 1 and 0 <= nc <= N - 1:
            board[nr][nc] += small_sand
        else:
            total_result += small_sand
    # 전진 방향 + 좌우 방향
    for dr, dc, ratio in [[mr * 2, mc * 2, 0.05], [-mc, -mr, 0.07], [mc, mr, 0.07], [-mc * 2, -mr * 2, 0.02], [mc * 2, mr * 2, 0.02]]:
        nr = r + dr
        nc = c + dc
        small_sand = int(board[r][c] * ratio)
        remain_sand -= small_sand
        if 0 <= nr <= N - 1 and 0 <= nc <= N - 1:
            board[nr][nc] += small_sand
        else:
            total_result += small_sand
    # 바로 앞 전진 방향
    nr = r + mr
    nc = c + mc
    if 0 <= nr <= N - 1 and 0 <= nc <= N - 1:
        board[nr][nc] += remain_sand
    else:
        total_result += remain_sand
    board[r][c] = 0 # 토네이도가 이번에 이동한 위치에서 모래는 없어야함!!!
    # print(board)
print(total_result)
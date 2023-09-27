# 180min 소요

n, m, k = list(map(int, input().split()))
gun_board = [[[] for _ in range(n)] for _ in range(n)]
for r in range(n):
    line = list(map(int, input().split()))
    for c in range(n):
        gun_board[r][c] = [line[c]]
# print(gun_board)
players = []
player_board = [[0 for _ in range(n)] for _ in range(n)]
for i in range(m):
    r, c, d, s = list(map(int, input().split()))
    player_board[r-1][c-1] = [d, s, 0, 0, i]
    players.append([r-1, c-1])
# print(players)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
# 라운드 반복
for _ in range(k):
    # 플레이어 순서대로 이동
    for p, (r, c) in enumerate(players): # enumerate에서 list 원소가 여러개인 경우, idx, (a, b, c...) 이런식으로 묶어줘야함!!!
        # print(player_board[r][c])
        player_info = player_board[r][c] # 참조 연산!!!
        player_dir = player_info[0]
        # 기존 방향대로 이동 준비
        nr = r + dr[player_dir]
        nc = c + dc[player_dir]
        # 벽을 마주한 경우 : 기존 방향과 반대로 이동
        if nr < 0 or n <= nr or nc < 0 or n <= nc:
            player_dir = (player_dir + 2) % 4
            nr = r + dr[player_dir]
            nc = c + dc[player_dir]
        player_info[0] = player_dir # 요렇게 해도 원본이 바뀌네!!!
        # print(player_board[r][c])
        # 사람을 마주한 경우 : 전투
        if player_board[nr][nc] != 0:
            n_player_info = player_board[nr][nc]
            # print(n_player_info)
            # 스코어 카운트 + 진 플레이어는 총 내려두고, 기존 방향대로 이동 + 이긴 플레이어 총 바꾸기 (벽 or 사람을 마주하는 경우 90도 시계방향 회전 후 이동)
            player_power_sum = player_info[1] + player_info[2]
            n_player_power_sum = n_player_info[1] + n_player_info[2]
            if (player_power_sum < n_player_power_sum) or ((player_power_sum == n_player_power_sum) and player_info[1] < n_player_info[1]):
                win_player_info = n_player_info
                lose_player_info = player_info
                win_origin_coor = [nr, nc, n_player_info[4]]
                lose_origin_coor = [r, c, player_info[4]]
            else:
                win_player_info = player_info
                lose_player_info = n_player_info
                win_origin_coor = [r, c, player_info[4]]
                lose_origin_coor = [nr, nc, n_player_info[4]]
            # 초기 세팅 # 이렇게 위쪽에 해두지 않으면 아래 player_board[nnr][nnc] != 0 연산에서 현재 플레이어가 원래 기존 위치에 있다고 인식을 해버려서 미리 0으로 바꿔서 현재 플레이어가 길을 가로막지 않도록 해줘야함!!!
            lose_origin_r, lose_origin_c, lose_origin_idx = lose_origin_coor
            win_origin_r, win_origin_c, win_origin_idx = win_origin_coor
            player_board[lose_origin_r][lose_origin_c] = 0
            player_board[win_origin_r][win_origin_c] = 0
            # 스코어 카운트
            win_player_info[3] += abs(player_power_sum - n_player_power_sum)
            # 총 내려두기
            lose_player_gun_power = lose_player_info[2] # 참조 연산인가???
            lose_player_dir = lose_player_info[0] # 참조 연산인가???
            if lose_player_gun_power != 0:
                gun_board[nr][nc].append(lose_player_gun_power)
                lose_player_info[2] = 0 # !!!
            # 기존 방향대로 이동 준비
            nnr = nr + dr[lose_player_dir]
            nnc = nc + dc[lose_player_dir]
            # 벽을 마주한 경우 or 사람을 마주한 경우 : 90도 시계방향 회전
            while (nnr < 0 or n <= nnr or nnc < 0 or n <= nnc) or player_board[nnr][nnc] != 0:
                lose_player_dir = (lose_player_dir + 1) % 4
                nnr = nr + dr[lose_player_dir]
                nnc = nc + dc[lose_player_dir]
            lose_player_info[0] = lose_player_dir # !!!

            player_board[nnr][nnc] = lose_player_info
            players[lose_origin_idx] = [nnr, nnc]
            
            # 진 플레이어 총 바꾸기 # 이긴 플레이어는 무기 바꿔놓고 여기는 누락시키면 안되지!!!
            if gun_board[nnr][nnc]:
                max_gun_power = max(gun_board[nnr][nnc])
                gun_board[nnr][nnc].remove(max_gun_power)  # remove 원소를 수행하면 제일 처음 원소 1개만 지워지나???
                lose_player_info[2] = max_gun_power  # !!!

            # 이긴 플레이어 총 바꾸기
            if gun_board[nr][nc]: # gun_board[nr][nc] 안에 아무 원소도 없으면 max 함수 사용 불가능!!!
                max_gun_power = max(gun_board[nr][nc])
                win_player_gun_power = win_player_info[2]
                if win_player_gun_power < max_gun_power:
                    if win_player_gun_power != 0:
                        gun_board[nr][nc].append(win_player_gun_power)
                    gun_board[nr][nc].remove(max_gun_power) # remove 원소를 수행하면 제일 처음 원소 1개만 지워지나???
                    win_player_info[2] = max_gun_power # !!!

            player_board[nr][nc] = win_player_info
            players[win_origin_idx] = [nr, nc]
        # 사람을 마주하지 않은 경우 : 총 줍기
        else:
            if gun_board[nr][nc]:  # gun_board[nr][nc] 안에 아무 원소도 없으면 max 함수 사용 불가능!!!
                max_gun_power = max(gun_board[nr][nc])
                if player_info[2] < max_gun_power:
                    if player_info[2] != 0:
                        gun_board[nr][nc].append(player_info[2])
                    gun_board[nr][nc].remove(max_gun_power)  # remove 원소를 수행하면 제일 처음 원소 1개만 지워지나???
                    player_info[2] = max_gun_power
            player_board[r][c] = 0 # 이게 else문 바로 아래에 있으면 max_gun_power가 업데이트 되지 않음. 위치 주의!!!
            player_board[nr][nc] = player_info
            players[p] = [nr, nc]
        # print(gun_board)
        # print(player_board)

# 스코어 최종 결과
print(' '.join([str(player_board[r][c][3]) for r, c in players]))
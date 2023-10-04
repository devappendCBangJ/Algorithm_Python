# 225min 소요

# 입력 받기
N, M, K = list(map(int, input().split()))
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

people_board = [[set() for _ in range(N)] for _ in range(N)]
people_coor = []
people_com = [0 for _ in range(M)]
people_com_count = 0
for m in range(M):
    pr, pc = list(map(lambda x: int(x)-1, input().split())) # 문제에서 제시한 좌표계와 코드의 좌표계는 다름!!!
    people_coor.append([pr, pc])
    people_board[pr][pc].add(m)

exit_coor = list(map(lambda x: int(x)-1, input().split()))

# print(board)
# print(people_coor)
# print(exit_coor)

# 참가자 움직임
def move(distance, people_com_count): # 참조인가??? 복사인가??? 복사임!!!
    er, ec = exit_coor
    # print(people_coor, people_com, exit_coor)
    for pi, (pr, pc) in enumerate(people_coor):
        # 목적지에 도착하지 않은 참가자의 경우
        if people_com[pi] == 0:
            mr = er - pr
            mc = ec - pc
            drdc_list = []
            # 움직임 판단
            if mr == 0 or mc == 0:
                if mr == 0:
                    drdc_list =[[mr, mc//abs(mc)]]
                elif mc == 0:
                    drdc_list = [[mr//abs(mr), mc]]
            else: # 대각선 방향이면, mr, mc 방향으로 이동하는 것이 아니라, [행, 0], [0, 열] 방향으로 1칸씩 움직여봐야함!!!
                drdc_list.append([mr//abs(mr), 0])
                drdc_list.append([0, mc//abs(mc)])
            # 실제 움직임
            for dr, dc in drdc_list:
                nr = pr + dr
                nc = pc + dc
                if nr == er and nc == ec:
                    people_com[pi] = 1
                    people_com_count += 1
                    # print(people_board[pr][pc], pi)
                    people_board[pr][pc].remove(pi) # pi를 m으로 써뒀네 실수!!!
                    distance += 1
                    if people_com_count == M:
                        return True, distance, people_com_count
                    break
                elif board[nr][nc] == 0:
                    people_coor[pi] = [nr, nc]
                    # print(pr, pc, nr, nc, people_board[pr][pc], pi)
                    people_board[pr][pc].remove(pi)
                    people_board[nr][nc].add(pi) # 이동하는데 remove는 해두고, 새로운 위치에 add를 안해줬네!!! [nr, nc]인데, [nr, pc]라고 오타냄!!!
                    distance += 1
                    # print(people_board)
                    break
    return False, distance, people_com_count

# 격자 회전을 위한 사각형 범위 판단
def square_range_decision():
    er, ec = exit_coor
    square_length = 1000000000 # 이거를 for문 안에 넣으면, 참가자를 불러올 때마다 square 길이를 초기화해버림!!!
    square_range = [[0, 1000000000], [0, 1000000000]] # 이거를 for문 안에 넣으면, 참가자를 불러올 때마다 square 범위를 초기화해버림!!!
    for pi, (pr, pc) in enumerate(people_coor):
        # 목적지에 도착하지 않은 참가자의 경우
        if people_com[pi] == 0:
            amr = abs(pr - er)
            amc = abs(pc - ec)
            # 사각형 범위 판단
            min_r = min(pr, er)
            max_r = max(pr, er)
            min_c = min(pc, ec)
            max_c = max(pc, ec)
            if amr <= amc: # 여기와 아래의 순서가 바뀌었음!!! 열의 길이가 더 길면, 열의 길이를 고정해야지!!!
                start_c = min_c
                end_c = max_c
                start_r = max(min_r - ((max_c - min_c) - (max_r - min_r)), 0)
                end_r = start_r + (max_c - min_c)
            else:
                start_r = min_r
                end_r = max_r
                start_c = max(min_c - ((max_r - min_r) - (max_c - min_c)), 0)
                end_c = start_c + (max_r - min_r)
            new_square_length = end_c - start_c + 1
            # print(square_length, new_square_length)
            if new_square_length < square_length:
                square_length = new_square_length
                square_range = [[start_r, end_r], [start_c, end_c]]
            elif new_square_length == square_length:
                if start_r < square_range[0][0]:
                    square_length = new_square_length
                    square_range = [[start_r, end_r], [start_c, end_c]]
                elif start_r == square_range[0][0]:
                    if start_c < square_range[1][0]:
                        square_length = new_square_length
                        square_range = [[start_r, end_r], [start_c, end_c]]
    return square_range

# 사각형 격자 회전
def square_rotate(square_range):
    er, ec = exit_coor
    [[start_r, end_r], [start_c, end_c]] = square_range # 이렇게 해도 되나??? 되네!!!
    # print(start_r, end_r, start_c, end_c)
    square_length = end_c - start_c + 1
    rotated_board = [[0 for _ in range(square_length)] for _ in range(square_length)]
    rotated_people_board = [[set() for _ in range(square_length)] for _ in range(square_length)]
    # board 업데이트 준비 + 경우에 따른 업데이트
    for ri, r in enumerate(range(start_r, end_r + 1)):
        for ci, c in enumerate(range(start_c, end_c + 1)):
            # 장애물이 있는 경우
            if board[r][c] != 0:
                board[r][c] -= 1
            # 참가자가 있는 경우
            elif len(people_board[r][c]):
                for pi in people_board[r][c]:
                    people_coor[pi] = [(c-start_c)+start_r, (square_length-1-(r-start_r))+start_c]
                    rotated_people_board[c-start_c][square_length-1-(r-start_r)].add(pi) # [ri, ci]가 아닌 회전된 좌표에 넣어야함!!!
            # 탈출구가 있는 경우
            elif r == er and c == ec:
                exit_coor[0] = (c-start_c)+start_r # exit_coor을 한번에 exit_coor = [] 바꾸려면 global로 선언해야됨. 근데 원소 단위로 바꾸면 global 선언 안해도 됨!!!
                exit_coor[1] = (square_length-1-(r-start_r))+start_c
            rotated_board[c-start_c][square_length-1-(r-start_r)] = board[r][c]
    # board 업데이트
    for ri, r in enumerate(range(start_r, end_r + 1)):
        for ci, c in enumerate(range(start_c, end_c + 1)):
            board[r][c] = rotated_board[ri][ci]
            people_board[r][c] = rotated_people_board[ri][ci] # rotate people board를 업데이트 해줘야함!!!

# 게임 K회 반복
distance = 0
for k in range(K): # K초가 지났다 = K초까지 완료했다
    is_complete, distance, people_com_count = move(distance, people_com_count)
    # print(distance)
    # print(k, board, people_board)
    if is_complete:
        break
    square_range = square_range_decision()
    square_rotate(square_range)

print(distance)
print(' '.join([str(coor+1) for coor in (exit_coor)])) # 문제에서 제시한 좌표계와 코드의 좌표계는 다름!!!

"""
# ---------------------------------------------------
# 다른 사람 풀이 -> 전체적으로 비슷. 회전하는 부분도 거의 유사
# 하지만, next_board를 통째로 만드는 부분, global 많이 선언, 정사각형 찾을 때 생성하는 부분 비효율적
# https://taemham.github.io/posts/CodeTree_BattleGround/#%EC%9D%B4%EB%8F%99-def-moveself
# ---------------------------------------------------
n, m, k = tuple(map(int, input().split()))
# 모든 벽들의 상태를 기록해줍니다.
board = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

for i in range(1, n + 1):
    board[i] = [0] + list(map(int, input().split()))

# 회전의 구현을 편하게 하기 위해 2차원 배열을 하나 더 정의해줍니다.
next_board = [ # 회전을 위해 최대 크기의 board를 하나 더 만드는 것은 비효율적!!!
    [0] * (n + 1)
    for _ in range(n + 1)
]

# 참가자의 위치 정보를 기록해줍니다.
traveler = [(-1, -1)] + [
    tuple(map(int, input().split()))
    for _ in range(m)
]

# 출구의 위치 정보를 기록해줍니다.
exits = tuple(map(int, input().split()))

# 정답(모든 참가자들의 이동 거리 합)을 기록해줍니다.
ans = 0

# 회전해야 하는 최소 정사각형을 찾아 기록해줍니다.
sx, sy, square_size = 0, 0, 0

# 모든 참가자를 이동시킵니다.
def move_all_traveler():
    global exits, ans # global을 너무 자주 사용해서 좋지 않음!!!

    # m명의 모든 참가자들에 대해 이동을 진행합니다.
    for i in range(1, m + 1):
        # 이미 출구에 있는 경우 스킵합니다.
        if traveler[i] == exits:
            continue
        
        tx, ty = traveler[i]
        ex, ey = exits

        # 행이 다른 경우 행을 이동시켜봅니다.
        if tx != ex:
            nx, ny = tx, ty

            if ex > nx: 
                nx += 1
            else:
                nx -= 1

            # 벽이 없다면 행을 이동시킬 수 있습니다.
            # 이 경우 행을 이동시키고 바로 다음 참가자로 넘어갑니다.
            if not board[nx][ny]:
                traveler[i] = (nx, ny)
                ans += 1
                continue

        # 열이 다른 경우 열을 이동시켜봅니다.
        if ty != ey:
            nx, ny = tx, ty

            if ey > ny: 
                ny += 1
            else:
                ny -= 1

            # 벽이 없다면 행을 이동시킬 수 있습니다.
            # 이 경우 열을 이동시킵니다.
            if not board[nx][ny]:
                traveler[i] = (nx, ny)
                ans += 1
                continue

# 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형을 찾습니다.
def find_minimum_square():
    global exits, sx, sy, square_size
    ex, ey = exits

    # 가장 작은 정사각형부터 모든 정사각형을 만들어봅니다.
    for sz in range(2, n + 1): # 정사각형을 엄청나게 많이 만들어보고, 출구와 참가자가 있는지 확인하므로 매우 비효율적!!!
        # 가장 좌상단 r 좌표가 작은 것부터 하나씩 만들어봅니다.
        for x1 in range(1, n - sz + 2):
            # 가장 좌상단 c 좌표가 작은 것부터 하나씩 만들어봅니다.
            for y1 in range(1, n - sz + 2):
                x2, y2 = x1 + sz - 1, y1 + sz - 1

                # 만약 출구가 해당 정사각형 안에 없다면 스킵합니다.
                if not (x1 <= ex and ex <= x2 and y1 <= ey and ey <= y2):
                    continue

                # 한 명 이상의 참가자가 해당 정사각형 안에 있는지 판단합니다.
                is_traveler_in = False
                for l in range(1, m + 1):
                    tx, ty = traveler[l]
                    if x1 <= tx and tx <= x2 and y1 <= ty and ty <= y2:
                        # 출구에 있는 참가자는 제외합니다.
                        if not (tx == ex and ty == ey):
                            is_traveler_in = True

                # 만약 한 명 이상의 참가자가 해당 정사각형 안에 있다면
                # sx, sy, square_size 정보를 갱신하고 종료합니다.
                if is_traveler_in:
                    sx = x1
                    sy = y1
                    square_size = sz

                    return

# 정사각형 내부의 벽을 회전시킵니다.
def rotate_square():
    # 우선 정사각형 안에 있는 벽들을 1 감소시킵니다.
    for x in range(sx, sx + square_size): # 처음부터 벽돌을 감소시켜두고 시작하니 편한듯!!!
        for y in range(sy, sy + square_size):
            if board[x][y]: 
                board[x][y] -= 1

    # 정사각형을 시계방향으로 90' 회전합니다.
    for x in range(sx, sx + square_size):
        for y in range(sy, sy + square_size):
            # Step 1. (sx, sy)를 (0, 0)으로 옮겨주는 변환을 진행합니다. 
            ox, oy = x - sx, y - sy
            # Step 2. 변환된 상태에서는 회전 이후의 좌표가 (x, y) . (y, square_n - x - 1)가 됩니다.
            rx, ry = oy, square_size - ox - 1
            # Step 3. 다시 (sx, sy)를 더해줍니다.
            next_board[rx + sx][ry + sy] = board[x][y]

    # next_board 값을 현재 board에 옮겨줍니다.
    for x in range(sx, sx + square_size):
        for y in range(sy, sy + square_size):
            board[x][y] = next_board[x][y]

# 모든 참가자들 및 출구를 회전시킵니다.
def rotate_traveler_and_exit():
    global exits

    # m명의 참가자들을 모두 확인합니다.
    for i in range(1, m + 1):
        tx, ty = traveler[i]
        # 해당 참가자가 정사각형 안에 포함되어 있을 때에만 회전시킵니다.
        if sx <= tx and tx < sx + square_size and sy <= ty and ty < sy + square_size: # 참가자들을 전부 돌면서 회전을 따로 시키니까 편한듯!!!
            # Step 1. (sx, sy)를 (0, 0)으로 옮겨주는 변환을 진행합니다. 
            ox, oy = tx - sx, ty - sy
            # Step 2. 변환된 상태에서는 회전 이후의 좌표가 (x, y) . (y, square_n - x - 1)가 됩니다.
            rx, ry = oy, square_size - ox - 1
            # Step 3. 다시 (sx, sy)를 더해줍니다.
            traveler[i] = (rx + sx, ry + sy)

    # 출구에도 회전을 진행합니다.
    ex, ey = exits
    if sx <= ex and ex < sx + square_size and sy <= ey and ey < sy + square_size:
        # Step 1. (sx, sy)를 (0, 0)으로 옮겨주는 변환을 진행합니다. 
        ox, oy = ex - sx, ey - sy
        # Step 2. 변환된 상태에서는 회전 이후의 좌표가 (x, y) . (y, square_n - x - 1)가 됩니다.
        rx, ry = oy, square_size - ox - 1
        # Step 3. 다시 (sx, sy)를 더해줍니다.
        exits = (rx + sx, ry + sy)


for _ in range(k):
    # 모든 참가자를 이동시킵니다.
    move_all_traveler()

    # 모든 사람이 출구로 탈출했는지 판단합니다.
    is_all_escaped = True
    for i in range(1, m + 1):
        if traveler[i] != exits:
            is_all_escaped = False

    # 만약 모든 사람이 출구로 탈출했으면 바로 종료합니다.
    if is_all_escaped: 
        break

    # 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형을 찾습니다.
    find_minimum_square()

    # 정사각형 내부의 벽을 회전시킵니다.
    rotate_square()
    # 모든 참가자들 및 출구를 회전시킵니다.
    rotate_traveler_and_exit()

print(ans)

ex, ey = exits
print(ex, ey)
"""
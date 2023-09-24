# 220min 소요

# 입력 받기
N, M = list(map(int, input().split()))
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
action = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for _ in range(M):
    action.append(list(map(int, input().split())))
# print(action)

# 연속된 구슬 불러오기
i = 0
move_len = 0
r, c = N//2, N//2 # 문제에서 주어진 좌표계는 (1,1)부터 시작하는데, 우리는 (0, 0)부터 시작이므로 문제에서 주어진 좌표계에서 조금 수정해야함!!!
# print(r, c)
val_list = []
coor_list = []
seq_dr = [0, 1, 0, -1]
seq_dc = [-1, 0, 1, 0]
end = False
while end == False:
    for dir in range(4):
        if i % 2 == 0:
            move_len += 1
        for _ in range(move_len):
            r += seq_dr[dir]
            c += seq_dc[dir]
            # print(r, c)
            val_list.append(board[r][c])
            coor_list.append([r, c])
            if r == 0 and c == 0:
                end = True
                break
        i += 1
        if end == True:
            break
# print(val_list)
# print(coor_list)

# 마법 시전
boom_val_dic = {1:0, 2:0, 3:0}
for d, s in action:
    # 마법 시전
    r, c = N // 2, N // 2
    d -= 1
    for s_len in range(s):
        r += dr[d]
        c += dc[d]
        for coor_idx, coor in enumerate(coor_list): # zip으로 val_list를 불러온 후에, 특정 원소의 값을 바꿔도, 실제 배열에서는 안바뀜. 인덱스로 접근해서 바꿔야함!!!
            if coor[0] == r and coor[1] == c:
                val_list[coor_idx] = 0
    # print(val_list)

    # 배열 빈칸 채우기
    i = 0 # 초기화 필수!!!
    new_val_list = [0 for _ in range(N**2-1)]
    for val in val_list:
        if val != 0:
            new_val_list[i] = val
            i += 1
    val_list = new_val_list.copy()
    # print(val_list)

    # 연속된 구슬 폭파 시퀀스
    pre_boom = True
    while pre_boom:
        # 연속된 구슬 폭파
        pre_boom = False
        count = 0
        for i in range(1, N**2-1):
            if val_list[i] == 0: # 원소에 0이 있는 경우 고려X!!!
                break
            if val_list[i-1] == val_list[i]:
                if count == 0:
                    start_idx = i-1
                count += 1
            else:
                if 3 <= count: # 이전과 같을 때 count를 1개씩만 올리기 때문에, 실제 4개가 중복될 때 count가 3이 됨!!!
                    pre_boom = True
                    boom_val_dic[val_list[i-1]] += count+1
                    for vi in range(start_idx, start_idx+count+1): # val_list[start_idx:start_idx+count] = 0 이런 식으로 한번에 할당하려면 우변도 배열 형식이여야함!!!
                        val_list[vi] = 0
                count = 0
        if 3 <= count:
            pre_boom = True
            boom_val_dic[val_list[i-1]] += count+1
            for vi in range(start_idx, N**2-1):
                val_list[vi] = 0

        # 배열 빈칸 채우기
        i = 0  # 초기화 필수!!!
        new_val_list = [0 for _ in range(N ** 2 - 1)]
        for val in val_list:
            if val != 0:
                new_val_list[i] = val
                i += 1
        val_list = new_val_list.copy()
        # print(val_list)
    # print(val_list)
    
    # 구슬 변화
    new_val_list = [0 for _ in range(N ** 2 - 1)]
    i = 0
    count = 1 # count가 0부터 시작하면, a개가 중복되었을 때 a-1개만 개수가 세지므로, 처음부터 1로 둠!!!
    for vi in range(1, N ** 2 - 1):
        if val_list[vi] == 0: # 원소에 0이 있는 경우 고려X!!! 범위 넘어가면 멈춰!!!
            break
        if val_list[vi - 1] == val_list[vi]:
            count += 1
        else:
            if i < N**2 - 1:
                new_val_list[i] = count
                i += 1
            if i < N**2 - 1:
                new_val_list[i] = val_list[vi - 1]
                i += 1
            count = 1
    if val_list[vi-1] != 0: # val_list[vi-1]이 0이면, 해당 인덱스 이후의 모든 값은 0이여야함. 하지만 이 조건문이 없으면 원소값이 0이여도 count 1이라고 할당이 되어서 문제 발생!!!
        if i < N**2 - 1:
            new_val_list[i] = count
            i += 1
        if i < N**2 - 1:
            new_val_list[i] = val_list[vi - 1] # 위에서 val_list[vi] == 0일 때 break해서 여기에 온 것일 수도 있으니까 val_list[-1]이 아니라, val_list[vi-1]을 사용해야함!!!
            i += 1
    val_list = new_val_list.copy() # 연산 전부 마쳤으면 val_list에 복사해야지!!!
    # print(val_list)

# print(boom_val_dic)
print(boom_val_dic[1] + boom_val_dic[2] * 2 + boom_val_dic[3] * 3)

"""
# ---------------------------------------------------
# 다른 사람 풀이 -> 거의 비슷한데, 조금 더 비효율적
# https://kimjingo.tistory.com/171
# ---------------------------------------------------
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
magics = [tuple(map(int, input().split())) for _ in range(M)]
 
n2loc = {} # 번호 -> 좌표
loc2n = {} # 좌표 -> 번호
n2ball = [-1] * N**2 # 번호 -> 번호에 해당하는 공 번호
result = 0
 
def print_ball(): # 디버그
    for i in range(N):
        print([n2ball[loc2n[(i, j)]] for j in range(N)])
    print()
 
def init_grid():
    # 2차원 좌표 정보를 1차원으로 변경
    # :return:

    global n2loc, loc2n
 
    # 우 하 좌 상
    dy_temp = (0, 1, 0, -1)
    dx_temp = (1, 0, -1, 0)
 
    loc = (0, -1) # 시작을 (0, -1)로 해서 (0, 0)에서 부터 시작하도록
    cnt = N ** 2 - 1 #  마지막 번호 = N^2-1
    dist, dist_change_flag = N, 1 # 처음 이동거리 N, 이동거리 변화 Flag
    dir = 0
 
    while True:
        for i in range(dist):
            ny = loc[0] + dy_temp[dir]
            nx = loc[1] + dx_temp[dir]
 
            loc = (ny, nx) # 좌표 갱신
            n2loc[cnt] = (ny, nx)  # 번호 -> 좌표       # 번호 -> 좌표, 좌표 -> 번호, 번호 -> 구슬 번호 변환을 위한 리스트 따로 관리!!!
            loc2n[(ny, nx)] = cnt # 좌표 -> 번호
            n2ball[cnt] = board[ny][nx] # 번호 -> 구슬 번호
            cnt -= 1
 
        dir = (dir + 1) % 4 # 방향 번경
        dist_change_flag += 1
        if dist_change_flag == 2: # 방향을 2번 변경하면 dist 1 감소
            dist_change_flag = 0
            dist -= 1
 
        if dist == 0: break # 거리가 0이 되면 종료
 
def arrangement():
    # 파괴된 구슬을 정리 (빈 칸에 구슬들을 채움)
    # :return:

    global n2ball
    del_cnt = n2ball.count(-1)
    n2ball = [ball for ball in n2ball if ball != -1] # -1(빈 칸)을 제외하고 다시 n2ball 배열 생성        # 리스트 컴프리헨션으로 해도 되네!!!
    n2ball.extend([0]*del_cnt) # 제외된 칸이 있기 때문에 그만큼 다시 배열을 채워줌
 
def destroy(d, s):          # 함수로 관리해서 return값만 지정해주면 반복문에서 break하기가 훨씬 쉬움!!!
    # 방향과 거리에 따라서 구슬들을 파괴함
    # :param d: 방향
    # :param s: 거리
    # :return:
    
    # 상하좌우
    dy = ("", -1, 1, 0, 0)
    dx = ("", 0, 0, -1, 1)
 
    shark_loc = (int(N / 2), int(N / 2)) # 상어 좌표
    y, x = shark_loc
    # 거리 상에 존재하는 구슬 모두 파괴
    for i in range(1, s+1, 1):
        ny = y + dy[d] * i
        nx = x + dx[d] * i
 
        n = loc2n[(ny, nx)] # 좌표 -> 번호를 얻음
        n2ball[n] = -1 # 해당 번호의 구슬 값을 -1(빈칸)으로 변경
 
def destroy2():
    # 연속하는 구슬 삭제
    # :return: 구슬 삭제 여부(True or False)
    global result
    ret = False # 구슬이 하나도 파괴되지 않은 경우 False 반환
 
    cnt = 0
    target = 0 # 같은 구슬인지 비교할 대상의 번호
    ball_num = 0 # 해당 번호의 구슬의 숫자
 
    for i in range(N**2): # 0~N^2-1번 까지 연속하는 구슬인지 조사
        if n2ball[i] == n2ball[target]: # 연속하는 경우
            cnt += 1
        else:
            # 연속하지 않는 경우
            if cnt >= 4: # 4개 이상 연속한다면
                ret = True
                for n in range(target, i, 1): # 해당 번호의 구슬 삭제
                    n2ball[n] = -1
                result += ball_num * cnt # 점수 추가
            # count, 비교 대상, 번호의 구슬 숫자 초기화
            cnt = 1             # cnt를 0이 아닌 1로 두고 했네. for idx를 0부터 시작해서 가능한 방법!!!
            target = i
            ball_num = n2ball[i]
 
    return ret # True or False 반환
 
def translate_all_balls():
    # 구슬 변화, 연속하는 구슬을 '구슬 개수', '구슬 번호'로 변환하여 n2ball에 추가함

    global n2ball
    new_n2ball = [0] # 새로운 n2ball, 첫 인덱스에 상어를 의미하는 공백 추가
    group = [] # 연속하는 구슬 저장용 배열
    for n in range(1, N**2, 1):
        if not group: group.append(n2ball[n]) # group이 []이면 n번째의 구슬 추가
        elif n2ball[n] == group[0]: # group에 들어있는 구슬 번호가 같은경우
            group.append(n2ball[n]) # 현재 구슬 추가          # 굳이 구슬을 저장하지 않아도 될듯. 연속되면 count만 하면 됨!!! 
        else:
            # group에 들어있는 구슬이 다른 경우(연속된 구슬의 종료 시점)
            new_n2ball.append(len(group)) # 구슬의 개수
            new_n2ball.append(group[0]) # 구슬의 번호를 차례대로 추가
            group = [n2ball[n]] # group을 원소를 현재 구슬로 초기화(뒷 loop 부터는 현재 원소를 기준으로 탐색)
 
    n2ball = [0] * N ** 2 # n2ball 초기화 후 new_n2ball을 복사함            # new_n2ball을 한번에 다 계산하고, 나중에 한번에 배열로 옮겨 담음으로써, 배열을 넘어가는 원소에 대한 관리가 쉬워짐!!!
    for i in range(len(new_n2ball)):
        if i >= (N ** 2): break # 번호가 넘어가는 경우 break
        n2ball[i] = new_n2ball[i]
 
def solve():
    # 1. 격자 초기화
    init_grid()
    for d, s in magics:
        # 2. 방향과 거리를 기준으로 구슬 파괴
        destroy(d, s)
        # 3. 파괴된 구슬 정리
        arrangement()
        # 4. 연속하는 구슬 파괴 및 정리
        while True:
            if not destroy2(): break
            arrangement()
        # 5. 구슬 변화
        translate_all_balls()
        # print_ball()
 
solve()
print(result)
"""
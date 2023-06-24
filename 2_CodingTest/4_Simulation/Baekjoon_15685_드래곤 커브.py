N = int(input())
curves = []
for _ in range(N):
    curves.append(list(map(int, input().split())))

board = [[0 for _ in range(101)] for _ in range(101)] # 실제 문제에서 주어진 Grid는 101개이고, 우리가 생각하는 배열의 순서와 같다!

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for x, y, d, g in curves:
    temp_curves = [[x, y]]
    for i in range(g+1):
        if i == 0:
            if 0 <= x + dx[d] < 101 and 0 <= y + dy[d] < 101: # N은 Grid 크기가 아니라, 드래곤 커브의 개수이다!
                temp_curves.append([x + dx[d], y + dy[d]])
        else:
            base_x, base_y = temp_curves[-1]
            temp_curves.extend([[base_x + (base_y - n_y), base_y - (base_x - n_x)] for n_x, n_y in reversed(temp_curves[:-1]) if 0 <= base_x + (base_y - n_y) < 101 and 0 <= base_y - (base_x - n_x) < 101]) # temp_curves[:-1:-1] 이렇게 하니까 안되네?  # N은 Grid 크기가 아니라, 드래곤 커브의 개수이다! # 실제 문제에서 주어진 Grid는 101개이고, 우리가 생각하는 배열의 순서와 같다!
            # new_temp_curves = list(map(lambda n_x, n_y: [base_x + (base_y - n_y), base_y - (base_x - n_x)], temp_curves[:-1]))
    # print(temp_curves)
    for x, y in temp_curves:
        board[y][x] = 1

count = 0
for x in range(101-1):
    for y in range(101-1):
        if board[y][x] == 1 and board[y][x+1] == 1 and board[y+1][x] == 1 and board[y+1][x+1] == 1:
            count += 1
print(count)
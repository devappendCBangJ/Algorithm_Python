
# ==============================================================
# 1) for loop 사용자 입력
# ==============================================================
# (1) 사용자 입력 받기 (Split + 형변환)
n, m = map(int, input().split())
arr = []
for _ in range(m):
    arr.append(list(map(int, input().split())))

# ==============================================================
# 2) 파일 입력
# ==============================================================
# (1) 라이브러리 불러오기
import sys

# (2) 표준 입력 : 파일로 설정 + 파일 읽기
sys.stdin = open("input.txt", "r")

# (3) 표준 입력이 파일이므로, input 함수는 파일을 읽음
n, m = map(int, input().split())

# (4) 파일 입력 받기 (Split + 형변환)
arr = [list(map(int, input().split())) for _ in range(m)]

# ==============================================================
# 3) 사용자 입력 빠르게 받기
# ==============================================================
# (1) 라이브러리 불러오기
import sys

# (2) 사용자 입력 받기 (Split + 형변환)
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline())) for _ in range(m)]
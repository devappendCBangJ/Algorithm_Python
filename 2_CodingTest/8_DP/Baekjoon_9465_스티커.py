# 60min 소요

test_count = int(input())
for _ in range(test_count):
    # 초기 정보 받기
    stickers = []
    n = int(input())
    stickers.append(list(map(int, input().split())))
    stickers.append(list(map(int, input().split())))

    # dp_table 초기화
    dp_table = [[0 for _ in range(n)], [0 for _ in range(n)]]
    dp_table[0][0] = stickers[0][0]
    dp_table[1][0] = stickers[1][0]

    # dp_table 업데이트 (점화식 적용)
    for c in range(1, n):
        dp_table[0][c] = max(dp_table[0][c-1], stickers[0][c] + dp_table[1][c-1])
        dp_table[1][c] = max(dp_table[1][c - 1], stickers[1][c] + dp_table[0][c - 1])
    
    # 최종 출력
    print(max(dp_table[0][n-1], dp_table[1][n-1]))

"""
# ---------------------------------------------------
# 다른 사람 풀이 -> 점화식 차이 있음. 이 점화식이 사람이 생각하는 방식과 더 가까움
# https://codesyun.tistory.com/185
# ---------------------------------------------------
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]

    # 2행 DP배열 형성
    DP = [[0] * N for _ in range(2)]

    # 스티커 길이가 1일 경우
    DP[0][0] = arr[0][0]
    DP[1][0] = arr[1][0]
    if N == 1:
        print(max(DP[0][0], DP[1][0]))
        continue

    # 스티커 길이가 2일 경우
    DP[0][1] = arr[1][0] + arr[0][1]
    DP[1][1] = arr[0][0] + arr[1][1]
    if N == 2:
        print(max(DP[0][1], DP[1][1]))
        continue

    # 스티커 길이가 3이상일 경우
    for i in range(2, N):
        # 메인 아이디어
        DP[0][i] = max(DP[1][i - 2], DP[1][i - 1]) + arr[0][i]
        DP[1][i] = max(DP[0][i - 2], DP[0][i - 1]) + arr[1][i]

    print(max(DP[0][-1], DP[1][-1]))
"""
# 5min 소요 -> 15min 소요

import sys
import heapq
input = sys.stdin.readline # input을 반복문으로 받을 때, input = sys.stdin.readline을 반드시 사용해야함. 그렇지 않으면 시간초과 나는 경우 많음!!!

N = int(input())
heap = []
for _ in range(N):
    val = int(input())
    if val == 0:
        out = 0
        if len(heap):
            out = heapq.heappop(heap)
        print(out)
    else:
        heapq.heappush(heap, val)
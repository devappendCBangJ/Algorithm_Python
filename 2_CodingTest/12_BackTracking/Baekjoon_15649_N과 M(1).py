from itertools import permutations

N, M = list(map(int, input().split()))

per_list = list(permutations(range(1, N+1), M))
for per in per_list:
    for p in per:
        print(p, end=' ')
    print()
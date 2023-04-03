# 라이브러리 불러오기
from itertools import combinations

# input 불러오기
L, C = map(int, input().split())
all_char = input().split()

# 변수 초기화
result = []
mother_len = 0

# 순열 조합 생성
for i in combinations(all_char, L):
    # 모음 개수 : 1개 이상, 자음 개수 : 2개 이상인 경우만 result에 추가
    for j in list(i):
        if j in ['a', 'e', 'i', 'o', 'u']:
            mother_len += 1
    if mother_len >= 1 and len(i) - mother_len >= 2:
        result.append(''.join(sorted(i)))
    # mother_len 초기화
    mother_len = 0

# 결과 정렬 + 출력
result = sorted(result)
for r in result:
    print(r)
from collections import deque

d = deque([1, 2, 3])
d.append(4)					# deque의 오른쪽에 4를 더함.
d.append(0)					# deque의 왼쪽에 0을 더함.
d.pop()						# deque의 가장 오른쪽 값을 지우고 반환함.
d.popleft()					# deque의 가장 왼쪽 값을 지우고 반환함.
d.extend([4, 5, 6])			# deque의 오른쪽에 iterable 한 객체의 원소들을 더함.
d.extendleft([-2, -1, 0])	# deque의 왼쪽에 iterable 한 객체의 원소들을 더함.
d.reverse()					# deque의 원소들의 순서를 뒤집음.
d.rotate(1)					# deque의 원소들의 순서를 한 칸씩 회전 시킴.
d[3]						# deque의 3번째 원소를 반환함.
d.clear()					# deque의 값을 비움.

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

import heapq

h = []
heapq.heappush(h, 3)	# 첫 번째 파라미터에는 list 객체가
heapq.heappush(h, 9)	# 두 번째 파라미터에는 삽입하려는 객체가 들어간다.
heapq.heappush(h, 7)
heapq.heappush(h, 8)
heapq.heappush(h, 5)
heapq.heappush(h, 1)

for _ in range(6):
	print(heapq.heappop(h))	# 작은 값부터 출력된다.

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

import heapq

h = []
heapq.heappush(h, -3)	# 첫 번째 파라미터에는 list 객체가
heapq.heappush(h, -9)	# 두 번째 파라미터에는 삽입하려는 객체가 들어간다.
heapq.heappush(h, -7)	# 단, 원래 넣으려는 값에 -를 붙여주고
heapq.heappush(h, -8)	# 출력시에도 -을 붙여준다.
heapq.heappush(h, -5)
heapq.heappush(h, -1)

for _ in range(6):
	print(-heapq.heappop(h))	# 큰 값부터 출력된다.

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

import heapq

h = [3, 9, 1, 4, 2]
heapq.heapify(h)	# 파라미터로 list 객체를 받는다.

for _ in range(6):
	print(-heapq.heappop(h))	# 작은 값부터 출력된다.
graph = {
    'A': {'B': 8, 'C': 1, 'D': 2, 'F': 5},
    'B': {'A': 8, 'C': 5},
    'C': {'A': 1, 'B': 5, 'D': 2},
    'D': {'A': 2, 'C': 2, 'E': 3, 'F': 5},
    'E': {'D': 3, 'F': 1},
    'F': {'A': 5, 'D': 5, 'E': 1}
}

# 그래프 : 본인 노드 이름 : {연결된 노드 이름 : 연결된 노드까지의 거리}
# distances : 시작 노드에서 특정 노드까지 거리
# start : 시작 노드
# heap : 다음 특정 노드 저장
# distance : 특정 노드까지 최소 거리
# current distance : 특정 노드까지 거리
# current destination : 특정 노드 노드명

import heapq  # 우선순위 큐 구현을 위함

def dijkstra(graph, start):
    # 초기값
    distances = {node: float('inf') for node in graph} # [시작 노드에서 특정 노드까지 거리] : 무한대
    distances[start] = 0 # [시작 노드에서 시작 노드까지 거리] : 0
    # print(distances) # 확인용 코드
    queue = [] # [정보 저장 heap] 생성
    heapq.heappush(queue, [distances[start], start])  # [[시작 노드에서 시작 노드까지 거리], [시작 노드명]]를 [정보 저장 heap]에 저장
    # print(distances[start], start) # 확인용 코드

    while queue:  # heap에서 노드가 빌 때까지 반복
        current_distance, current_destination = heapq.heappop(queue) # [정보 저장 heap]에서 가장 작은 [[시작 노드에서 특정 노드까지 거리], [특정 노드명]] 빼기
        # print(current_distance, current_destination)
        if distances[current_destination] < current_distance: # 가장 작은 [시작 노드에서 특정 노드까지 거리]가 [기존 시작 노드에서 특정 노드까지 거리]보다 크면 건너띔
            print(distances[current_destination], current_distance)
            continue

        for new_destination, new_distance in graph[current_destination].items(): # [특정 노드]에 연결된 [[특정 노드에서 다음 특정 노드까지 거리], [다음 특정 노드명]] 전부 돌기
            distance = current_distance + new_distance # [시작 노드에서 다음 특정 노드까지의 새로운 거리] = [정보 저장 heap]에서 가장 작은 [[시작 노드에서 특정 노드까지 거리], [특정 노드명]] + 특정 노드명에 연결된 [[특정 노드에서 다음 특정 노드까지 거리], [다음 특정 노드명]]
            if distance < distances[new_destination]: # [시작 노드에서 다음 특정 노드까지 거리] > [시작 노드에서 다음 특정 노드까지의 새로운 거리]라면
                distances[new_destination] = distance # [시작 노드에서 다음 특정 노드까지 거리] 최신화
                heapq.heappush(queue, [distance, new_destination]) # [[시작 노드에서 다음 특정 노드까지 거리], [다음 특정 노드명]]을 [정보 저장 heap]에 저장

    return distances

print(dijkstra(graph, 'A'))
"""
Dijkstra 알고리즘

출발점 -> 모든 노드 최단 거리를 계산하는 알고리즘
"""

import heapq

# queue = []
# heapq.heappush(queue, [2, 'A'])
# heapq.heappush(queue, [5, 'B'])
# heapq.heappush(queue, [1, 'C'])
# heapq.heappush(queue, [7, 'D'])
#
# print(queue)
#
# for i in range(len(queue)):
#     print(heapq.heappop(queue))


graph = {
    'A': {'B': 8, 'C': 1, 'D': 1},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5},
}

def dijkstra(graph, start_node):
    # {'A': inf, 'B': inf, 'C': inf, 'D': inf, 'E': inf, 'F': inf}
    dp = {node: float('inf') for node in graph}
    # 초기화
    dp[start_node] = 0
    queue = []
    heapq.heappush(queue, [dp[start_node], start_node])

    while queue:
        current_dist, current_node = heapq.heappop(queue)

        if current_dist > dp[current_node]:
            continue

        for adjacent, weight in graph[current_node].items():
            dist = current_dist + weight
            if dist < dp[adjacent]:
                dp[adjacent] = dist
                heapq.heappush(queue, [dp[adjacent], adjacent])

    return dp

print(dijkstra(graph, 'A'))



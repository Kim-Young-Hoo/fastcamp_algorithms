"""
Node : 위치
Edge : 노드간의 관계를 표시한 선 방향이 있을 수도 없응ㄹ 수도 있음
Degree : Node에 연결된 무방향 Edge의 개수
In-Degree : Node로 향한 방향 Edge의 개수
Out-Degree : Node 밖으로 가는 Edge 수
Path Length : 경로를 구성하기 위해 사용된 Edge 수
Simple Path : 중복정점이 없는 경로
Cycle : Simple Path의 시작과 끝이 동일한 경우

방향그래프 : 양방향 이동이 가능한 그래프
            A <-> B는 (A,B)로 표기
무방향그래프 : 한방향 이동만 가능한 그래프
            A -> B는 <A,B>로 표기기
가중치그래프 : 간선에 비용이 있는 그래프

구현은 dict랑 list로 한다
"""

graph = {}

graph["A"] = ["B", "C"]
graph["B"] = ["A", "D"]
graph["C"] = ["A", "G", "H", "I"]
graph["D"] = ["B", "E", "F"]
graph["E"] = ["D"]
graph["F"] = ["D"]
graph["G"] = ["C"]
graph["H"] = ["C"]
graph["I"] = ["C", "J"]
graph["J"] = ["I"]

# BFS 구현
# visited는 queue, need_visit도 queue
def bfs_mine(graph, start_node):
    visited = [start_node] # queue
    need_visit = [start_node] # queue

    while True:

        if len(visited) == len(graph):
            break

        visit = need_visit.pop(0)

        for ele in graph[visit]:
            if ele not in visited:
                need_visit.append(ele)
                visited.append(ele)
    return visited



def bfs_lecture(graph, start_node):
    visited = []
    need_visit = [start_node]

    while need_visit:

        node = need_visit.pop(0)

        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited


print(bfs_mine(graph, "A"))
print(bfs_lecture(graph, "A"))
"""
시간복잡도는 O(V+E)
"""


# dfs 구현
# visited는 queue, need_visit은 stack
def dfs_mine(graph, start_node):
    visited = [] # queue
    need_visit = [start_node] # stack


    while need_visit:
        node = need_visit.pop()

        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited
print(dfs_mine(graph, "A"))











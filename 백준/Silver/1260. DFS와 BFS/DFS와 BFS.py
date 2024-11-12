# 입력 받기
N, M, start = map(int, input().split())  # N: 정점 개수, M: 간선 개수, start: 시작 정점

from collections import deque
def dfs(graph, start, visited, result):
    visited[start] = True  # 시작 정점 방문 처리
    result.append(start)   # 방문한 정점 기록
    for neighbor in graph[start]:
        if not visited[neighbor]:  # 방문하지 않은 정점만 탐색
            dfs(graph, neighbor, visited, result)

def bfs(graph, start, visited, result):
    queue = deque([start])  # 시작 정점을 큐에 넣기
    visited[start] = True    # 시작 정점 방문 처리
    while queue:
        node = queue.popleft()  # 큐에서 하나씩 꺼내기
        result.append(node)      # 방문한 정점 기록
        for neighbor in graph[node]:
            if not visited[neighbor]:  # 방문하지 않은 정점만 큐에 넣기
                visited[neighbor] = True
                queue.append(neighbor)

                
graph = [[] for _ in range(N + 1)]  # 그래프 초기화 (1-based index)

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    graph[i].sort()

# 방문 기록을 위한 리스트
visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

# DFS 탐색
dfs_result = []
dfs(graph, start, visited_dfs, dfs_result)

# BFS 탐색
bfs_result = []
bfs(graph, start, visited_bfs, bfs_result)

# 결과 출력
print(" ".join(map(str, dfs_result)))
print(" ".join(map(str, bfs_result)))
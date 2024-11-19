N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

parent = [0] * (N + 1)
 
from collections import deque
def find_parents():
    queue = deque([1])
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if parent[neighbor] == 0: 
                parent[neighbor] = current 
                queue.append(neighbor)

find_parents()

for i in range(2, N + 1):
    print(parent[i])
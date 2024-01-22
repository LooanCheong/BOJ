from collections import deque

n, m, k = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def bfs(k):
    q = deque([k])
    visited[k] = True
    bfs_list.append(k)

    while q:
        node = q.popleft()

        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                bfs_list.append(i)

def dfs(k):
    visited[k] = True

    for i in graph[k]:
        if not visited[i]:
            dfs_list.append(i)
            dfs(i)




dfs_list = [k]
dfs(k)
visited = [False for _ in range(n + 1)]
bfs_list = []
bfs(k)

for i in dfs_list:
    print(i, end = ' ')

print()

for i in bfs_list:
    print(i, end = ' ')
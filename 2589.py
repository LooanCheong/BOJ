from collections import deque

n, m = map(int, input().split())
land = []

for _ in range(n):
    land.append(list(input()))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

ans = 0

def bfs(start_x, start_y):
    global ans

    visited = [[-1] * m for _ in range(n)]
    visited[start_x][start_y] = 0
    q = deque([(start_x, start_y)])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == "L" and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    ans = max(ans, max(map(max, visited)))

for i in range(n):
    for j in range(m):
        if land[i][j] == "L":
            bfs(i, j)

print(ans)
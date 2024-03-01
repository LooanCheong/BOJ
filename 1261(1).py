import heapq

m, n = map(int, input().split())
INF = int(1e9)

land = [list(map(int, input())) for _ in range(n)]
dis = [[INF for _ in range(m)] for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = []

heapq.heappush(q, (0, 0, 0))
dis[0][0] = 0

while q:
    cost, x, y = heapq.heappop(q)

    if dis[x][y] < cost:
        continue

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and cost + land[nx][ny] < dis[nx][ny]:
            dis[nx][ny] = land[nx][ny] + cost
            heapq.heappush(q, (dis[nx][ny], nx, ny))

print(dis[n - 1][m - 1])
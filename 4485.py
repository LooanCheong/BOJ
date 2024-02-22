import heapq

INF = int(1e9)
cnt = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while True:
    cnt += 1

    n = int(input())

    if n == 0:
        break

    land = [list(map(int, input().split())) for _ in range(n)]
    dis = [[INF] * n for _ in range(n)]

    q = []
    heapq.heappush(q, (land[0][0], 0, 0))
    dis[0][0] = land[0][0]

    while q:
        cost, x, y = heapq.heappop(q)

        if x == y == n - 1:
            print("Problem %d: %d" % (cnt, dis[x][y]))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                new_cost = cost + land[nx][ny]

                if new_cost < dis[nx][ny]:
                    dis[nx][ny] = new_cost
                    heapq.heappush(q, (new_cost, nx, ny))
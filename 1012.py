from collections import deque

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())

    land = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())

        land[y][x] = 1


    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    def bfs(start_x, start_y):
        q = deque([(start_x, start_y)])
        land[start_x][start_y] = 0

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1:
                    land[nx][ny] = 0
                    q.append((nx, ny))


    cnt = 0
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)
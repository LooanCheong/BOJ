from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

land = list(list(map(int, input().split())) for _ in range(n))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

shark = 2
shark_exp = 0


def bfs(a, b):
    q = deque([(a, b)])
    dis[a][b] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and dis[nx][ny] == -1 and (land[nx][ny] <= shark or land[nx][ny] == 9):
                dis[nx][ny] = dis[x][y] + 1
                q.append((nx, ny))


def find_shark():
    for i in range(n):
        for j in range(n):
            if land[i][j] == 9:
                return i, j


ans = 0
INF = 10 ** 9

while True:
    if shark_exp == shark:
        shark += 1
        shark_exp = 0

    dis = list([-1 for _ in range(n)] for _ in range(n))

    find_shark()
    x, y = find_shark()
    bfs(x, y)

    check = INF
    check_i = 0
    check_j = 0

    for i in range(n):
        for j in range(n):
            if dis[i][j] != 0 and dis[i][j] != -1 and land[i][j] != 0 and land[i][j] < shark:
                if dis[i][j] < check:
                    check = dis[i][j]
                    check_i = i
                    check_j = j

    if check != INF:
        ans += check
        land[check_i][check_j] = 9
        land[x][y] = 0
        shark_exp += 1

    elif check == INF:
        break

print(ans)
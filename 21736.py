n, m = map(int, input().split())

land = [list(input()) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def dfs(x, y):
    global cnt
    if land[x][y] == "P":
        cnt += 1
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and land[nx][ny] != "X" and visited[nx][ny] == False:
            dfs(nx, ny)


cnt = 0

for i in range(n):
    for j in range(m):
        if land[i][j] == "I":
            dfs(i, j)

if cnt == 0:
    print("TT")
else:
    print(cnt)
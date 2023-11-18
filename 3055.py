from collections import deque

r, c = map(int, input().split())

land = [list(input()) for _ in range(r)]
dis = [([0] * c) for _ in range(r)]
q = deque()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(start_x, start_y):
    dis[start_x][start_y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and (land[nx][ny] == "." or land[nx][ny] == "D") and land[x][y] == "S":
                dis[nx][ny] = dis[x][y] + 1
                land[nx][ny] = "S"
                q.append((nx, ny))

            elif 0 <= nx < r and 0 <= ny < c and (land[nx][ny] == "." or land[nx][ny] == "S") and land[x][y] == "*":
                land[nx][ny] = "*"
                q.append((nx, ny))


for i in range(r):
    for j in range(c):
        if land[i][j] == "D":
            beaver_x = i
            beaver_y = j

        elif land[i][j] == "S":
            start_x, start_y = i, j
            q.appendleft((i, j))

        elif land[i][j] == "*":
            q.append((i, j))

bfs(start_x, start_y)

if dis[beaver_x][beaver_y]:
    print(dis[beaver_x][beaver_y])

else:
    print("KAKTUS")

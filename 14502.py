from collections import deque
import copy

n, m = map(int, input().split())
land = [list(map(int, input().split())) for i in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

ans = 0
wall_cnt = 0

def make_wall(wall_cnt):
    if wall_cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if land[i][j] == 0:
                land[i][j] = 1
                make_wall(wall_cnt + 1)
                land[i][j] = 0

def bfs():
    q = deque()
    copy_land = copy.deepcopy(land)

    for i in range(n):
        for j in range(m):
            if copy_land[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and copy_land[nx][ny] == 0:
                copy_land[nx][ny] = 2
                q.append((nx, ny))

    global ans
    cnt = 0

    for i in range(n):
        for j in range(m):
            if copy_land[i][j] == 0:
                cnt += 1
    ans = max(ans, cnt)


make_wall(wall_cnt)
print(ans)
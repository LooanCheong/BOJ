from collections import deque

n, k = map(int, input().split())

tube = []
vi = []

for i in range(n):
    tube.append(list(map(int, input().split())))

    for j in range(n):
        if tube[i][j] != 0:
            vi.append((tube[i][j], 0, i, j))

vi.sort()
q = deque(vi)

s, x, y = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while q:
    num, cnt, tmp_x, tmp_y = q.popleft()

    if cnt == s:
        break

    for i in range(4):
        nx = tmp_x + dx[i]
        ny = tmp_y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and tube[nx][ny] == 0:
            tube[nx][ny] = num
            q.append((num, cnt + 1, nx, ny))

print(tube[x - 1][y - 1])
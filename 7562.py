from collections import deque

t = int(input())

for i in range(t):
    l = int(input())

    start = list(map(int, input().split()))
    dest = list(map(int, input().split()))

    dis = [[-1 for _ in range(l)] for _ in range(l)]

    dx = [1, 1, -1, -1, 2, 2, -2, -2]
    dy = [2, -2, 2, -2, 1, -1, 1, -1]

    #bfs
    q = deque([(start[0], start[1])])
    dis[start[0]][start[1]] = 0

    while q:
        x, y = q.popleft()

        if x == dest[0] and y == dest[1]:
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l and dis[nx][ny] == -1:
                dis[nx][ny] = dis[x][y] + 1
                q.append([nx, ny])

    print(dis[dest[0]][dest[1]])
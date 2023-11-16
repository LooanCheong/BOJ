from collections import deque

n, l, r = map(int, input().split())

people = list(list(map(int, input().split())) for _ in range(n))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(start_x, start_y):
    temp = []
    q = deque([(start_x, start_y)])
    temp.append((start_x, start_y))
    visited[start_x][start_y] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and l <= abs(
                    people[x][y] - people[nx][ny]) <= r:
                visited[nx][ny] = True
                q.append((nx, ny))
                temp.append((nx, ny))
    return temp


ans = 0

while True:
    visited = [list(False for _ in range(n)) for _ in range(n)]
    check = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                country = bfs(i, j)

                if len(country) > 1:
                    check = 1
                    num = sum([people[x][y] for x, y in country]) // len(country)

                    for x, y in country:
                        people[x][y] = num

    if check == 0:
        break

    ans += 1

print(ans)

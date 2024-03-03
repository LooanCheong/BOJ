n, m = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]
dis = [[0] * m for _ in range(n)]

dis[0][0] = land[0][0]

for i in range(1, m):
    dis[0][i] = dis[0][i - 1] + land[0][i]

for i in range(1, n):
    dis[i][0] = dis[i - 1][0] + land[i][0]

for i in range(1, n):
    for j in range(1, m):
        dis[i][j] = max(dis[i - 1][j], dis[i][j - 1]) + land[i][j]

print(dis[n - 1][m - 1])
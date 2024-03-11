n = int(input())

land = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == j == n - 1:
            break

        if j + land[i][j] < n:
            dp[i][j + land[i][j]] += dp[i][j]

        if i + land[i][j] < n:
            dp[i + land[i][j]][j] += dp[i][j]

print(dp[-1][-1])
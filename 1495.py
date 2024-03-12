n, s, m = map(int, input().split())
v = list(map(int, input().split()))
dp = [[0] * (m + 1) for _ in range(n + 1)]

dp[0][s] = 1

for i in range(n):
    for j in range(m + 1):
        if dp[i][j] == 1:
            min_v = j - v[i]
            max_v = j + v[i]

            if min_v >= 0:
                dp[i + 1][min_v] = 1

            if max_v <= m:
                dp[i + 1][max_v] = 1

ans = -1

for i in range(m, -1, -1):
    if dp[n][i] == 1:
        ans = i
        break

print(ans)
n = int(input())

stair = [0]
dp = [0 for _ in range(n + 1)]

for _ in range(n):
    stair.append(int(input()))

dp[1] = stair[1]

for i in range(2, n + 1):
    if i == 2:
        dp[i] = dp[1] + stair[2]

    else:
        dp[i] = max(dp[i - 2], dp[i - 3] + stair[i - 1]) + stair[i]

print(dp[n])
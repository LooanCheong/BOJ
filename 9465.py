t = int(input())

for _ in range(t):
    n = int(input())

    sticker = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0 for _ in range(n)] for _ in range(2)]

    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]

    for i in range(1, n):
        for j in range(2):
            if j == 0:
                dp[j][i] = max(dp[1][i - 1] + sticker[j][i], dp[0][i - 1])

            elif j == 1:
                dp[j][i] = max(dp[0][i - 1] + sticker[j][i], dp[1][i - 1])

    print(max(map(max, dp)))
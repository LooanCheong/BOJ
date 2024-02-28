n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0, 0] for _ in range(3)] for _ in range(n)]

for i in range(3):
    for j in range(2):
        dp[0][i][j] = board[0][i]

for i in range(1, n):
    dp[i][0][0] = min(dp[i - 1][0][0], dp[i - 1][1][0]) + board[i][0]
    dp[i][0][1] = max(dp[i - 1][0][1], dp[i - 1][1][1]) + board[i][0]

    dp[i][1][0] = min(dp[i - 1][0][0], dp[i - 1][1][0], dp[i - 1][2][0]) + board[i][1]
    dp[i][1][1] = max(dp[i - 1][0][1], dp[i - 1][1][1], dp[i - 1][2][1]) + board[i][1]

    dp[i][2][0] = min(dp[i - 1][2][0], dp[i - 1][1][0]) + board[i][2]
    dp[i][2][1] = max(dp[i - 1][2][1], dp[i - 1][1][1]) + board[i][2]

print(max(map(max, dp[-1])), min(map(min, dp[-1])))
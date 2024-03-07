n = int(input())

for i in range(n):
    num = int(input())
    dp = [1] * 10

    for j in range(num - 1):
        for k in range(10):
            dp[k] = sum(dp[k:])
    print(sum(dp))
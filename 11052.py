import copy

n = int(input())
card = [0] + list(map(int, input().split()))
dp = copy.deepcopy(card)

for i in range(2, n + 1):
    for j in range(i):
        if i - j >= j:
            dp[i] = max(dp[i], dp[i - j] + dp[j])

print(dp[n])
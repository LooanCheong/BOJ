h, w = map(int, input().split())
block = list(map(int, input().split()))

ans = 0
cnt = 0
max_block = 0
idx = 0

for i in range(len(block)):
    if block[i] >= max_block:
        max_block = block[i]
        idx = i
        ans += cnt
        cnt = 0

    else:
        cnt += max_block - block[i]

cnt = 0
max_block = 0

for i in range(len(block) - 1, idx - 1, -1):
    if block[i] >= max_block:
        max_block = block[i]
        idx = i
        ans += cnt
        cnt = 0

    else:
        cnt += max_block - block[i]

print(ans)
from collections import deque

f, s, g, u, d = map(int, input().split())

floor = [-1] * (f + 1)

floor[s] = 0

q = deque([s])

while q:
    now = q.popleft()

    for i in (now + u, now - d):
        if 0 < i <= f and floor[i] == -1:
            floor[i] = floor[now] + 1
            q.append(i)

print(floor[g] if floor[g] != -1 else "use the stairs")
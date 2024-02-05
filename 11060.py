from collections import deque

n = int(input())
a = list(map(int, (input().split())))
dis = [-1] * n

dis[0] = 0

if n > 1:
    q = deque([(0, a[0])])

    while q:
        now, jump = q.popleft()

        for i in range(1, jump + 1):
            if now + i < n and dis[now + i] == -1:
                dis[now + i] = dis[now] + 1
                q.append((now + i, a[now + i]))

print(dis[-1])
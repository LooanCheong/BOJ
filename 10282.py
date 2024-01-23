import heapq

INF = int(1e9)

t = int(input())

for _ in range(t):
    n, d, c = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(d):
        a, b, s = map(int, input().split())

        graph[b].append((a, s))

    dis = [INF] * (n + 1)

    q = []
    dis[c] = 0

    heapq.heappush(q, (0, c))

    while q:
        dist, node = heapq.heappop(q)

        if dis[node] < dist:
            continue

        for i in graph[node]:
            cost = dist + i[1]

            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    cnt = 0
    time = 0

    for i in dis:
        if i != INF:
            cnt += 1
            time = max(time, i)

    print(cnt, time)
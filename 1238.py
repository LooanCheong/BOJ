import heapq

n, m, x = map(int, input().split())
city = [[] for _ in range(n + 1)]
INF = int(1e9)

for _ in range(m):
    dep, dest, cost = map(int, input().split())

    city[dep].append((dest, cost))

def dijkstra(start):
    q = []
    dis = [INF] * (n + 1)
    dis[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, node = heapq.heappop(q)

        if dis[node] < dist:
            continue

        for i in city[node]:
            cost = dist + i[1]

            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return dis

ans = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    if i == x:
        for j in range(1, len(dijkstra(x))):
            ans[j] += dijkstra(x)[j]
    else:
        ans[i] += dijkstra(i)[x]

print(max(ans))
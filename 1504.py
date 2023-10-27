import heapq

n, e = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())

    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

INF = int(1e9)

def dijkstra(start):
    dis = [INF] * (n + 1)
    q = []
    dis[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, node = heapq.heappop(q)

        if dis[node] < dist:
            continue

        for i in graph[node]:
            cost = dist + i[1]

            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return dis

v1_dis = dijkstra(1)[v1] + dijkstra(v1)[v2] + dijkstra(v2)[n]
v2_dis = dijkstra(1)[v2] + dijkstra(v2)[v1] + dijkstra(v1)[n]

ans = min(v1_dis, v2_dis)

print(ans if ans < INF else -1)
import heapq

INF = int(1e9)

V, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dis = [INF] * (V + 1)



def dijkstra(start):
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

dijkstra(start)

for i in range(1, V + 1):
    if dis[i] == INF:
        print("INF")
    else:
        print(dis[i])
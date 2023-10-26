import heapq

n = int(input())
m = int(input())
city = [[] for _ in range(n + 1)]

for _ in range(m):
    dep, dest, cost = map(int, input().split())

    city[dep].append((dest, cost))

start, final = map(int, input().split())

INF = int(1e9)
dis = [INF] * (n + 1)

q = []
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

print(dis[final])
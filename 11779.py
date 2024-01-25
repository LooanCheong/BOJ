import heapq

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
dis = [INF] * (n + 1)
prev_node = [0] * (n + 1)

for _ in range(m):
    dep, des, cost = map(int, input().split())

    graph[dep].append((des, cost))

start, end = map(int, input().split())

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
            prev_node[i[0]] = node
            heapq.heappush(q, (cost, i[0]))

path = [end]
tmp = end
while tmp != start:
    tmp = prev_node[tmp]
    path.append(tmp)

print(dis[end])
print(len(path))
for i in path[::-1]:
    print(i, end = " ")
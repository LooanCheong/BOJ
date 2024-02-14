n = int(input())
m = int(input())
people = [[] for _ in range(n + 1)]
invite = []

for _ in range(m):
    a, b = map(int, input().split())
    people[a].append(b)
    people[b].append(a)

friends = []

for i in people[1]:
    friends.append(i)
    invite.append(i)

for i in friends:
    for j in people[i]:
        if j != 1 and j not in invite:
            invite.append(j)

print(len(invite))
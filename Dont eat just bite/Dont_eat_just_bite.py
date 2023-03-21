n, m = input().strip().split()
stick, apple = [], []
for i in range(int(n)):
    stick.append(input())
for i in range(int(m)):
    apple.append(input())
x, z = input().strip().split()
apples = [0 for i in range(int(n)+1)]
#graph
edge = []
for i in range(int(n)):
    k = [int(stick[i].strip().split()[0]), int(i)+1, int(stick[i].strip().split()[1])]
    edge.append(k)
    k = [int(i)+1, int(stick[i].strip().split()[0]), int(stick[i].strip().split()[1])]
    edge.append(k)
    for j in range(int(m)):
        if int(apple[j].strip().split()[0]) == i and int(apple[j].strip().split()[1]) >= int(z):
            apples[i] = int(apple[j].strip().split()[1])
summ = 0
edge.sort()
#bellmanford
for p in range (int(n)):
    start = int(x)
    distance = [float('inf')]*(int(n)+1)
    distance[start] = 0
    for i in range(int(n)):
        for u, v, w in edge:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
    for i in range (int(n)+1):
        if apples[distance.index(min(distance))] != 0:
            x = distance.index(min(distance))
            summ += distance[x]
            apples[x] = 0
            break
        else:
            distance[distance.index(min(distance))] = float('inf')
print(summ)

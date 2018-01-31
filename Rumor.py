n,m = (int(i) for i in input().split())
priceMap = [None] + [int(i) for i in input().split()]
graph = {}

for _ in range(m):
	start, end = (int(i) for i in input().split())
	if start not in graph:
		graph[start] = [end]
	else:
		graph[start].append(end)

	if end not in graph:
		graph[end] = [start]
	else:
		graph[end].append(start)

visited = set()
cost = 0

def findFriends(i, graph, visited):
	stack = [i]
	minCost = priceMap[i]

	while stack:
		s = stack.pop()
		visited.add(s)
		for j in graph[s]:
			if j not in visited:
				stack.append(j)
				minCost = min(minCost, priceMap[j])

	return minCost

for i in range(1,n+1):
	if i not in visited:
		if i not in graph:
			minCost = priceMap[i]
			visited.add(i)
		else:
			minCost = findFriends(i, graph, visited)
		cost += minCost

print(cost)

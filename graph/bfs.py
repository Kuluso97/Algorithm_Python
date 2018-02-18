from graph import Graph 

def bfs(graph, source, visited):
	if source not in graph.vertex.keys():
		return

	visited.add(source)
	queue = [source]
	while queue:
		s = queue.pop(0)
		print(s, end = ' ')
		for i in graph.vertex[s]:
			if i not in visited:
				visited.add(i)
				queue.append(i)

def main():
	g = Graph()
	g.addEdge('A', 'B')
	g.addEdge('D', 'F')
	g.addEdge('D', 'E')
	g.addEdge('C', 'E')
	g.addEdge('A', 'C')
	g.addEdge('E', 'F')
	g.addEdge('C', 'F')

	visited = set()
	bfs(g, 'A', visited)


if __name__ == '__main__':
	main()
from graph import Graph

def dfs(graph, source, visited):

	if source not in graph.vertex.keys():
		return

	print(source, end=' ')
	
	visited.add(source)

	for i in graph.vertex[source]:
		if i not in visited:
			dfs(graph, i, visited)


def main():
	g = Graph()
	g.addEdge('A', 'B')
	g.addEdge('B', 'D')
	g.addEdge('D', 'F')
	g.addEdge('D', 'E')
	g.addEdge('B', 'E')
	g.addEdge('C', 'E')
	g.addEdge('A', 'C')
	g.addEdge('E', 'F')

	visited = set()
	dfs(g, 'A', visited)

if __name__ == '__main__':
	main()
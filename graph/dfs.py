class Graph:

	def __init__(self):
		self.vertex = {}

	def addEdge(self, start, end):
		if start not in self.vertex.keys():
			self.vertex[start] = [end]
		else:
			self.vertex[start].append(end)

		if end not in self.vertex.keys():
			self.vertex[end] = [start]
		else:
			self.vertex[end].append(start)

	def dfs(self, source):
		if source not in self.vertex.keys():
			return -1

		print(source, end=' ')
		visited = set()
		visited.add(source)
		for i in self.vertex[source]:
			self.dfsHelper(i, visited)

	def dfsHelper(self, source, visited):
		if source in visited: return
		visited.add(source)
		print(source, end=' ')

		for i in self.vertex[source]:
			if i not in visited:
				self.dfsHelper(i, visited)

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

	g.dfs('A')

if __name__ == '__main__':
	main()
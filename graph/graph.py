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
import heapq
import sys

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        ## the -1 is the item
        return heapq.heappop(self._queue)[-1]

    def isEmpty(self):
        return not self._queue

 
class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]
        self.visited = [False] * vertices
        self.parent = [None] * vertices
        self.dist = [float('inf')] * vertices
 
    # Funtion that implements Dijkstra's single source 
    # shortest path algorithm for a graph represented 
    # using adjacency matrix representation
    def dijkstra(self, src, dest):
        self.dist[src] = 0

        pq = PriorityQueue()
        pq.push(src, 0)

        while not pq.isEmpty():
            node = pq.pop()
            self.visited[node] = True

            for neighbour, distance in enumerate(self.graph[node]):
                if distance and not self.visited[neighbour] and \
                    self.dist[neighbour] > self.dist[node] + distance:
                    self.dist[neighbour] = self.dist[node] + distance
                    self.parent[neighbour] = node
                    pq.push(neighbour, self.dist[node] + distance)


    def printShortestPath(self, src, dest):
        self.dijkstra(src, dest)
        node = dest
        path = [str(dest)]
        while node != src:
            path.append(str(self.parent[node]))
            node = self.parent[node]

        print(' '.join(path[::-1]))


def main():
    ## Testing Priority Queue:

    # pq = PriorityQueue()
    # pq.push("First Item", 2)
    # pq.push("Second Item", 3)

    # print(pq.pop())
    # print(pq.pop())

    g  = Graph(9)
    g.graph = [
                [0, 4, 0, 0, 0, 0, 0, 8, 0],
                [4, 0, 8, 0, 0, 0, 0, 11, 0],
                [0, 8, 0, 7, 0, 4, 0, 0, 2],
                [0, 0, 7, 0, 9, 14, 0, 0, 0],
                [0, 0, 0, 9, 0, 10, 0, 0, 0],
                [0, 0, 4, 14, 10, 0, 2, 0, 0],
                [0, 0, 0, 0, 0, 2, 0, 1, 6],
                [8, 11, 0, 0, 0, 0, 1, 0, 7],
                [0, 0, 2, 0, 0, 0, 6, 7, 0]
              ]

    g.printShortestPath(0, 4)

if __name__ == '__main__':
    main()

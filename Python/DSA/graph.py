class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, src, dest):
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)

    def dfs(self, start):
        visited = [False for _ in range(self.num_vertices)]
        self._dfs(start, visited)

    def _dfs(self, v, visited):
        visited[v] = True
        print(v, end=' ')
        for neighbour in self.adj_list[v]:
            if not visited[neighbour]:
                self._dfs(neighbour, visited)

    def bfs(self, start):
        visited = [False for _ in range(self.num_vertices)]
        queue = []
        visited[start] = True
        queue.append(start)
        while queue:
            m = queue.pop(0)
            print(m, end=' ')
            for neighbour in self.adj_list[m]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append(neighbour)

g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Depth First Traversal:")
g.dfs(2)
print("\nBreadth First Traversal:")
g.bfs(2)
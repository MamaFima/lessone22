class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex, edge):
        if vertex in self.graph:
            self.graph[vertex].append(edge)
        else:
            self.graph[vertex] = [edge]

    def display(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_edge("A", "B")
g.add_edge("B", "A")
g.display()  # A: ['B'], B: ['A']
g.dfs("A")  # Поиск в глубину
print()
g.bfs("A")  # Поиск в ширину

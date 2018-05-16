from collections import defaultdict

class Graph:

    def __init__(self, n):
        self.graph = dict()
        for i in range(n):
            self.graph[i] = []

    def connect(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def find_distance(self, s):
        distances = [-1 for i in range(len(self.graph))]
        visited = [False] * len(self.graph)
        queue = []
        distances[s] = 0
        queue.append(s)
        visited[s] = True

        while queue:
            current_element = queue.pop(0)
            height = distances[current_element]
            for i in self.graph[current_element]:
                if visited[i] is False:
                    distances[i] = height + 6
                    queue.append(i)
                    visited[i] = True
        distances.pop(s)
        print(" ".join(map(str, distances)))

t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1)
    s = int(input())
    graph.find_distance(s-1)

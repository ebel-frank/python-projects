class Graph():
    def __init__(self, size):
        self.adj = []
        for i in range(1, size+1):
            self.adj.append([0 for i in range(size)])
        self.size = size

    def add_edge(self, orig, dest):
        if orig > self.size or dest > self.size or orig < 0 or dest < 0:
            print("Trying to add an invalid Edge!(%d, %d)"%(orig, dest))
        else:
            self.adj[orig-1][dest-1] = 1
            self.adj[dest-1][orig-1] = 1

    def remove_edge(self, orig, dest):
        if orig > self.size or dest > self.size or orig < 0 or dest < 0:
            print("Trying to remove an invalid Edge!(%d, %d)"%(orig, dest))
        else:
            self.adj[orig-1][dest-1] = 0
            self.adj[dest-1][orig-1] = 0

    def display(self):
        for row in self.adj:
            print()
            for val in row:
                print('{:4}'.format(val),end="")

# A sample graph
G = Graph(5)
G.add_edge(5,5)
G.add_edge(1,5)
G.add_edge(5,1)
G.add_edge(5,3)

G.display()

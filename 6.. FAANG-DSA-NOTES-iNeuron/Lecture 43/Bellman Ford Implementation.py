# Bellman Ford algorithm for finding shortest distance from single source Implementation

from collections import defaultdict
# Defining Graph class
class Graph:
    # defining constructor
    def __init__(self,vertices):
        self.V = vertices
        self.graph = []

    # defining addEdge function
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])

    # defining bellmanFord function which takes source node as argument
    def bellmanFord(self,source):
        # using dictionary to track the node and its distances from source node
        distances = defaultdict()
        # creating a set of allNodes to store unique nodes present in graph
        allNodes = set()

        # iterating through graph to store nodes in set
        for u,v,w in self.graph:
            allNodes.add(u)
            allNodes.add(v)

        # for every node assigning distance to infinity
        for items in allNodes:
            distances[items] = float("Inf")
        # for source node assigning distance to 0
        distances[source] = 0

        # iterating till allnodes(vertices)-1 times according to algorithm
        for _ in range(self.V-1):
            for u,v,w in self.graph:
                # if current starting point node's distance is not infinity and current node value and cost to 
                # reach destination node is less that destination node value then assign destination node value
                #  to current node value + cost to reach that node according to algorithm
                if distances[u]!=float("Inf") and distances[u]+w < distances[v]:
                    distances[v] = distances[u]+w


        # after iterating through all node present in graph, one more iteration we need to do to check graph contains negative edge weight
        for u,v,w in self.graph:
            if distances[u]!=float("Inf") and distances[u]+w < distances[v]:
                print("Negative edge weight found.")
                return

        # printing the distances of all nodes from source node
        print(distances)



g = Graph(7)
g.addEdge(1,2,6)
g.addEdge(1,3,5)
g.addEdge(1,4,5)
g.addEdge(2,5,-1)
g.addEdge(3,2,-2)
g.addEdge(3,5,1)
g.addEdge(4,3,-2)
g.addEdge(4,6,-1)
g.addEdge(5,7,3)
g.addEdge(6,7,3)

g.bellmanFord(1)  # Output - defaultdict(None, {1: 0, 2: 1, 3: 3, 4: 5, 5: 0, 6: 4, 7: 3})

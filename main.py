from graph_interface import Graph
import random

numOfNodes = 10
numOfEdges= 10

graph = Graph(numOfNodes)
for i in range(numOfEdges):
    graph.addEdge(random.randint(0,numOfNodes-1),random.randint(0,numOfNodes-1),random.randint(0,100))


graph.drawgraph()


from graph_interface import Graph
import random

numOfNodes = 20
numOfEdges= 10

graph = Graph(numOfNodes, numOfEdges)

graph.addEdge(0, 1, 10)
graph.addEdge(0, 2, 20)
graph.addEdge(0, 3, 30)
graph.addEdge(0, 2, 40)
graph.addEdge(0, 2, 40)




graph.drawgraph(4)
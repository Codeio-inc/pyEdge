#open a new window
import tkinter as tk  
from tkinter import *
import math
radius = 30

#create panel
root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()



# class for directed graph
class Graph:
    #constructor
    def __init__(self, vertices):
        self.V = vertices
        self.circle = {}
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
    
    import tkinter as tk

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph[u][v] = w

    # Returns true if there is a path from source 's' to sink 't' in
    # residual graph. Also fills parent[] to store the path
    def BFS(self, s, t, parent):
        # Mark all the vertices as not visited
        visited = [False] * (self.V)
        
        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
        
        # Standard BFS Loop
        while queue:
            # Dequeue a vertex from queue and print it
            u = queue.pop(0)
            
            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        
        # If we reached sink in BFS starting from source, then return
        # true, else false
        return True if visited[t] else False
    




    def drawgraph(self):

        # Define the radius and spacing of the circles
        radius = 30
        x_spacing = 150
        y_spacing = 150

        # Create circles for each vertex
        self.circles = []

        # Draw circles for each vertex
        for i in range(self.V):
            x = (i % 3) * x_spacing + radius + 50
            y = (i // 3) * y_spacing + radius + 50
            canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="white")
            self.circles.append(canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="white"))
            canvas.create_text(x, y, text=str(i), font="Arial 20 bold")
        
        # Draw arrows for each edge
        for i in range(self.V):
            for j in range(self.V):
                if self.graph[i][j] > 0:
                        # Calculate the coordinates of the centers of the circles
                        x1 = canvas.coords(self.circles[i])[0] + radius
                        y1 = canvas.coords(self.circles[i])[1] + radius
                        x2 = canvas.coords(self.circles[j])[0] + radius
                        y2 = canvas.coords(self.circles[j])[1] + radius
                        angle = math.atan2(y2 - y1, x2 - x1)

                        if x1 == x2 and y1 == y2:
                            canvas.create_oval(x1 + radius , y1 + (radius/2) , x1 + 3*radius, y1 - (radius/2), width=2, outline="black")
                            x1 = x1 + radius + 12
                            x2 = x2 + radius
                            y1 = y1 - 13
                            y2 = y2 
                            canvas.create_line(x1, y1 , x2 , y2 , arrow=tk.LAST, fill="black", width=1, arrowshape=(15,15,7) )
                            

                        else:
                            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                            x1 += math.cos(angle) * radius
                            y1 += math.sin(angle) * radius
                            x2 -= math.cos(angle) * radius
                            y2 -= math.sin(angle) * radius

                            if x1 == x2 and distance > y_spacing:
                                canvas.create_arc(x1 - radius, y1, x2 + radius, y2, start=90, extent=180, width=2, style=tk.ARC)
                            elif y1 == y2 and distance > x_spacing:
                                canvas.create_arc(x1, y1 - radius, x2, y2 + radius, start=0, extent=180, width=2, style=tk.ARC)
                            elif (round(math.degrees(angle)) == 45 or round(math.degrees(angle)) == -45) and distance > (math.sqrt(2) * x_spacing):
                                canvas.create_arc(x1 - radius, y1 - radius, x2 + radius, y2 + radius, start=0, extent=180, width=2, style=tk.ARC)

                            #get angle of line
                            else:
                                canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST, fill="black", width=2)
                        
        # Start the main loop to display the window
        root.mainloop()
    
    # Returns tne maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink):
        # This array is filled by BFS and to store path
        parent = [-1] * (self.V)

        max_flow = 0

        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent):
            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow += path_flow
            #change the color of the path used to red

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        
        return max_flow
    
    def on_circle_click(self, event):
        # Save the ID of the circle that was clicked
        self.selected_circle = event.widget.find_closest(event.x, event.y)[0]

    def on_circle_drag(self, event):
        # Move the selected circle to the new mouse position
        canvas.coords(self.selected_circle, event.x - radius, event.y - radius, event.x + radius, event.y + radius)

    



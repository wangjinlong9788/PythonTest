Adjacency List Python
There is a reason Python gets so much love. A simple dictionary of vertices and its edges is a sufficient representation of a graph. You can make the vertex itself as complex as you want.

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

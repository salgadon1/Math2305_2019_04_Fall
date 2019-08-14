import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class Graph(object):
    
    def __init__(self, *args):
 
        self.edge_list_file = ''
        self.edge_set = set()
        self.vertex_set = set()

        # 1 or 2 arguments may be passed.
        # if 1, it can either be a edge list file or an edge set
        if(len(args)==1):
            # if the argument is a string, read the edges from the file
            if(type(args[0]) is str):
                self.edge_list_file = args[0]
                self.edge_set = self.set_edges_from_file()
                self.update_vertices()
            
            # if the argument is a set, set the edge_set and create a 
            # vertex set from the endpoints of the edges+
            elif(type(args[0]) is set):
                self.edge_set = args[0]
                self.update_vertices()

        # if 2 arguments are passed, the first should be the vertex set
        # and the second the edge_set
        elif(len(args)==2):
            self.vertex_set = args[0]
            self.edge_set = args[1]
    
    def set_edges_from_file(self):
        """ Returns the set of edges """
        edge_set = set()
        edge_list = np.loadtxt(self.edge_list_file, int)   # numpy 2-d array
        for row in edge_list:
            e = (row[0],row[1])
            edge_set.add(e)     # Assign keys and values
        return edge_set
        
    
    def update_vertices(self):
        """ Returns the set of vertices """
        for e in self.edge_set:
            self.vertex_set = self.vertex_set.union(e)
   
    def add_edge(self,e):
        """ Add an edge to the graph """
        self.edge_set.add(e)
        self.update_vertices()
    
    def copy(self):
        """ Make a copy of the graph """
        edges = self.edge_set.copy()
        vertices = self.vertex_set.copy()
        return Graph(vertices, edges)
    
    def is_tree(self):
        """ Return True if the graph is a tree, False otherwise based on the |V|=|E|+1 criterion"""
        return len(self.vertex_set) == len(self.edge_set) + 1
    
    def spans(self,H):
        """ Return True if self spans the graph H , False otherwise """
        return self.vertex_set == H.vertex_set
    
    def draw_graph(self):
        """ This function is used to visualize your weighted graph. The functions
            used inside are from the networkx library. """
        
        G = nx.Graph()
        G.add_nodes_from(self.vertex_set)
        G.add_edges_from(self.edge_set)
        pos=nx.spring_layout(G) # positions for all nodes
        nx.draw_networkx_nodes(G,pos,node_size=250) # nodes
        nx.draw_networkx_edges(G,pos,edgelist=G.edges(),width=1) # edges
        nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')
        plt.axis('off')
        plt.show()
        
    def draw_subgraph(self, H):
        """ This function is used to visualize your weighted graph. The functions
            used inside are from the networkx library. """
        
        G = nx.Graph()
        G.add_nodes_from(self.vertex_set)
        G.add_edges_from(self.edge_set)

        S = nx.Graph()
        S.add_nodes_from(H.vertex_set)
        S.add_edges_from(H.edge_set)


        pos=nx.spring_layout(G) # positions for all nodes
        nx.draw_networkx_nodes(G,pos,node_size=250) # nodes
        nx.draw_networkx_nodes(G,pos, nodelist = S.nodes(),node_size=400)
        nx.draw_networkx_edges(G,pos,edgelist=G.edges(),width=1) # edges
        nx.draw_networkx_edges(G,pos,edgelist=S.edges(), color = 'red' ,width=5)
        
        # labels
        nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')
        plt.axis('off')
        plt.show()
        
        

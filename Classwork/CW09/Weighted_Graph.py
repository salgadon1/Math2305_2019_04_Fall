import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from Graph import Graph

class Weighted_Graph(Graph):
    
    def __init__(self, *args):
        
        self.edge_list_file = ''
        self.edge_dict = {}
        self.edge_set = set()
        self.vertex_set = set()
        
        # 1 or 2 arguments may be passed.
        # if 1, it can either be a edge list file or an edge dictionary
        if(len(args)==1):
            # if the argument is a string, read the edges from the file
            if(type(args[0]) is str):
                self.edge_list_file = args[0]
                self.edge_dict = self.set_edge_dict_from_file()
                self.edge_set = set()
                self.update_edges()
                self.vertex_set = set()
                self.update_vertices()
            
            # if the argument is a dictionary, set the edge dictionary and create a 
            # edge set from the dictionary and a vertex set from the edge set.
            elif(type(args[0]) is dict):
                self.edge_dict = args[0]
                self.edge_set = set()
                self.update_edges()
                self.vertex_set = set()
                self.update_vertices()

        # if 2 arguments are passed, the first should be the vertex set
        # and the second the edge dictionary
        elif(len(args)==2):
            self.vertex_set = args[0]
            self.edge_dict = args[1]
            self.edge_set = set()
            self.update_edges()

            
    def set_edge_dict_from_file(self):
        """ Reads in the edge list from the provided directory address and 
            creates a edge dictionary where the keys are the edges and values
            are the corresponding edge weights. In particular, to access the
            value of edge (a,b), simply type edge_dict[(a,b)]"""
        edge_dict = dict()                                 # dict()=empty dictionary
        edge_list = np.loadtxt(self.edge_list_file, int)   # numpy 2-d array
        for row in edge_list:
            edge_dict[(row[0], row[1])] = row[2]           # Assign keys and values
        return edge_dict
    
    
    def update_edges(self):
        """ Returns the set of edges """
        self.edge_set = set(self.edge_dict.keys())
        
    def copy(self):
        """ Make a copy of the graph """
        
        # if the edge list file has been defined, create the new graph from that
        if(self.edge_list_file):
            return Weighted_Graph(self.edge_list_file)
        # otherwise create the graph from the edge_dict and vertex_set
        else:
            edge_dict = self.edge_dict.copy()
            vertices = self.vertex_set.copy()
            return Weighted_Graph(vertices, edge_dict)
        
 
    def add_edge(self,e,w):
        """ add an edge with a weight """
        self.edge_dict[e] = w
        self.update_edges()
        self.update_vertices()
    
    def draw_graph(self):
        """ This function is used to visualize your weighted graph. The functions
            used inside are from the networkx library. """
        
        G = nx.read_edgelist(self.edge_list_file, nodetype=int, data=(('weight',float),))
        e=[(u,v) for (u,v,d) in G.edges(data=True)]
        pos=nx.spring_layout(G) # positions for all nodes
        nx.draw_networkx_nodes(G,pos,node_size=250) # nodes
        nx.draw_networkx_edges(G,pos,edgelist=e,width=1) # edges

        # labels
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        plt.axis('off')
        plt.show()
        
    def draw_subgraph(self, H):
        """ This function is used to visualize your weighted graph. The functions
            used inside are from the networkx library. """
        
        G = nx.read_edgelist(self.edge_list_file, nodetype=int, data=(('weight',float),))
        e1=[(u,v) for (u,v,d) in G.edges(data=True)]
        e2= [e for e in e1 if e in H.edge_set]
        v1 =[v for v in H.vertex_set]
        pos=nx.spring_layout(G) # positions for all nodes
        nx.draw_networkx_nodes(G,pos,node_size=250) # nodes
        nx.draw_networkx_nodes(G,pos, nodelist = v1,node_size=400)
        nx.draw_networkx_edges(G,pos,edgelist=e1,width=1) # edges
        nx.draw_networkx_edges(G,pos,edgelist=e2, color = 'red' ,width=5)
        
        # labels
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        plt.axis('off')
        plt.show()


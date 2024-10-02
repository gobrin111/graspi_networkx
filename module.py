import networkx as nx
import matplotlib.pyplot as plt
import math


def createGraph(txt):
    g = nx.Graph()
    g = nx.Graph(g) #makes sure that it is an undirect graph
    g.add_node(1,color='red')
    g.add_node(0,color='blue')
    nodeIndex = 2
    with open(txt,'r') as file:
        lines = file.readlines()
        metadata = lines[0].strip().split()
        x = int(metadata[0])
        y = int(metadata[1])
        row = lines[1].strip().split()
        for i in range(x): #creates bottom row of structure
            currentColor = 'white'
            if(row[i]=='0'):
                currentColor = 'black'
            g.add_node(nodeIndex,color=currentColor)
            g.add_edge(0,nodeIndex, weight=1) #connected all the bottom nodes to the blue element
            if(i!=0):
                g.add_edge(nodeIndex,nodeIndex-1, weight=1)
            nodeIndex+=1
        for a in range(y+1):
            if(a==0 or a==1): #skips over the metadata and the first row of the graph, since those two lines have already been processed
                continue
            row = lines[a].strip().split()
            for i in range(x):
                currentColor = 'white'
                if(row[i]=='0'):
                    currentColor = 'black'
                g.add_node(nodeIndex,color=currentColor)
                if(a==y):
                    g.add_edge(1,nodeIndex,weight=1) #connect top row to the red element
                g.add_edge(nodeIndex,nodeIndex-x,weight=1) #node below current node
                if(i!=0):
                    g.add_edge(nodeIndex,nodeIndex-1, weight=1) #node to the left of the current node
                    g.add_edge(nodeIndex,nodeIndex-(x+1), weight=math.sqrt(2)) #node to the bottom left of the current node
                if(i!=x-1):
                    g.add_edge(nodeIndex,nodeIndex-(x-1),weight=math.sqrt(2)) #node to the bottom right of the current node
                nodeIndex+=1
    return g


def filterGraph(inputG):
    filter_edges = []
    filtered_edges = [(u, v) for u, v, d in inputG.edges(data=True) if ((inputG.nodes[v]['color'] == 'black') and (inputG.nodes[u]['color'] == 'black')) or ((inputG.nodes[v]['color'] == 'red') and (inputG.nodes[u]['color'] == 'black')) or ((inputG.nodes[v]['color'] == 'black') and (inputG.nodes[u]['color'] == 'red')) or ((inputG.nodes[v]['color'] == 'white') and (inputG.nodes[u]['color'] == 'white')) or ((inputG.nodes[v]['color'] == 'white') and (inputG.nodes[u]['color'] == 'blue')) or ((inputG.nodes[v]['color'] == 'blue') and (inputG.nodes[u]['color'] == 'white'))]
    H = nx.Graph()
    H.add_nodes_from(inputG.nodes(data=True))
    H = inputG.edge_subgraph(filtered_edges)
    return H


def filtered_bfs(inputG):
    bfs_paths = nx.single_source_shortest_path(inputG, source=1)
    return bfs_paths
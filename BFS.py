import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


def load_dataset(file_path):     #load the dataset
    dataset = pd.read_csv(file_path, header=None, sep='\s+')
    return dataset.values.tolist()
def bfs(graph, visualize=True): #dfs algorithm
    num_nodes = len(graph)

    # Initialize visited nodes and distances
    visited = [False] * num_nodes
    distances = [float('inf')] * num_nodes

    # Start from the first node
    start_node = 0
    visited[start_node] = True
    distances[start_node] = 0
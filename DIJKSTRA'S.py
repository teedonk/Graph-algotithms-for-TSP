import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import heapq

def load_dataset(file_path):                #load dataset
    dataset = pd.read_csv(file_path, header=None, sep='\s+')
    return dataset.values.tolist()

def calculate_total_distance(path, graph):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += graph[path[i]][path[i + 1]]
    return total_distance
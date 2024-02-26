import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations

def load_dataset(file_path): #load the dataset
    dataset = pd.read_csv(file_path, header=None, sep='\s+')
    return dataset.values.tolist()
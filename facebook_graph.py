import networkx as nx
import gzip

# Function to load the graph from the gz file
def load_facebook_graph(file_path):
    G = nx.Graph()
    
    with gzip.open(file_path, 'rt') as f:
        for line in f:
            edge = line.strip().split()
            if len(edge) == 2:
                G.add_edge(int(edge[0]), int(edge[1]))

    return G

# Load the graph
file_path = 'facebook_combined.txt.gz'  # Update this path if necessary
G = load_facebook_graph(file_path)

# Calculate the average degree
degrees = dict(G.degree())
average_degree = sum(degrees.values()) / len(degrees)

# Calculate transitivity
transitivity = nx.transitivity(G)

# Calculate diameter
if nx.is_connected(G):
    diameter = nx.diameter(G)
else:
    diameter = None  # The graph might not be connected

# Calculate radius
if nx.is_connected(G):
    radius = nx.radius(G)
else:
    radius = None  # The graph might not be connected

# Display the results
print(f"Average Degree: {average_degree}")
print(f"Transitivity: {transitivity}")
print(f"Diameter: {diameter}")
print(f"Radius: {radius}")

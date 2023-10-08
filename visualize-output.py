import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.pyplot import Axes
from heapq import heappush, heappop
import json

def generate_graph(gd: dict) -> nx.Graph:
    gn = nx.Graph()

    for k in gd.keys():
        current_node = gd[k]

        for edge in current_node:
            gn.add_edge(k, edge[0], weight=edge[1])

    return gn

# Menggunakan algoritma A* untuk mencari jalur terpendek
def astar(graph, start, goal):
    visited = set()
    queue = [(0, start, [])]
    
    while queue:
        cost, node, path = heappop(queue)
        
        if node == goal:
            return path + [node]
        
        if node not in visited:
            visited.add(node)
            
            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    new_cost = cost + graph[node][neighbor]["weight"]
           
                    heappush(queue, (new_cost + heuristic[neighbor], neighbor, path + [node]))
    return []

def draw_graph(file_path: str, output_file: str = "", save_to_file: bool = False):
    # Visualisasi proses alur pencarian
    fig, ax = plt.subplots()
    ax.axis('off')
    pos: dict = nx.spring_layout(G, seed=7)
    edge_labels: dict = nx.get_edge_attributes(G, "weight")

    for node in G.nodes():
        if node in shortest_path:
            color = 'green'
        else:
            color = 'lightblue'
        nx.draw_networkx_nodes(G, pos, nodelist=[node], node_color=color, node_size=800)
        nx.draw_networkx_labels(G, pos, labels={node: node})
        
    for edge in G.edges():
        if edge[0] in shortest_path and edge[1] in shortest_path:
            color = 'green'
        else:
            color = 'gray'
        nx.draw_networkx_edges(G, pos, edgelist=[edge], edge_color=color, width=3, alpha=0.5)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    ax: Axes = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()

    # # Hitung nilai f(n) = g(n) + h(n) untuk setiap node
    # f_values = {}
    # for node in G.nodes():
    #     g_value = nx.shortest_path_length(G, source="S", target=node, weight="weight")
    #     h_value = heuristic[node]
    #     f_values[node] = g_value + h_value


    # # Tambahkan nilai f(n) pada setiap node
    # for node, value in f_values.items():
    #     x, y = pos[node]
    #     plt.text(x, y + 0.1, f'f={value}', ha='center', fontsize=8, bbox=dict(facecolor='white', alpha=0.5))

    # simpan graf
    if save_to_file:
        plt.savefig(output_file)
        print(f"Saved to {output_file}")
        return
    # Tampilkan graf
    plt.show()


# Inisialisasi graf
print("Graph Node Visualiation")
graph_file_path: str = 'soal/soal.json'
with open(graph_file_path) as gf:
        graph_json = json.load(gf)
graph_dict: dict = graph_json["graph"]
heuristic: dict = graph_json["heuristic"]

G = nx.Graph()

# Tambahkan node dan edge ke graf
G = generate_graph(graph_dict)
# for node, edges in graph_dict.items():
#     for edge in edges:
#         G.add_edge(node, edge[0], weight=edge[1])

# Buat posisi node menggunakan spring layout
pos = nx.spring_layout(G)

# Cari jalur terpendek
shortest_path = astar(G, "S", "Z")

# simpan hasil
draw_graph(file_path=graph_file_path, output_file="output/result", save_to_file=True)



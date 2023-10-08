import json
import os.path
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.pyplot import Axes
from networkx.classes import Graph

def generate_graph(gd: dict) -> Graph:
    gn = nx.Graph()

    for k in gd.keys():
        current_node = gd[k]

        for edge in current_node:
            gn.add_edge(k, edge[0], weight=edge[1])

    return gn

def draw_graph(file_path: str, output_file: str = "", save_to_file: bool = False):
    if output_file == "":
        output_file = "outputs/" + os.path.splitext(os.path.basename(file_path))[0] + ".png"

    with open(file_path) as gf:
        graph_json = json.load(gf)

    graph_dict: dict = graph_json["graph"]

    graph_net: Graph = generate_graph(graph_dict)

    pos: dict = nx.spring_layout(graph_net, seed=7)
    edge_labels: dict = nx.get_edge_attributes(graph_net, "weight")

    nx.draw_networkx_nodes(graph_net, pos, node_size=800)
    nx.draw_networkx_edges(graph_net, pos, width=3)
    nx.draw_networkx_edge_labels(graph_net, pos, edge_labels)
    nx.draw_networkx_labels(graph_net, pos, font_size=16, font_family="sans-serif")

    ax: Axes = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()

    # add table
    col_labels = ['node','h(n)']
    heuristic_dict: dict = graph_json["heuristic"]
    heuristic_dict_result = []
    i = 0
    for k in heuristic_dict.keys():
        heuristic_dict_result.append([k, heuristic_dict[k]])
        i += 1
    plt.table (cellText=heuristic_dict_result, colWidths=[0.1] * 3,
                     colLabels=col_labels,
                     loc='upper right')

    if save_to_file:
        plt.savefig(output_file)
        print(f"Saved to {output_file}")
        return

    plt.show()

if __name__ == '__main__':
    print("Graph Node Visualiation")
    graph_file_path: str = 'soal/soal.json'

    draw_graph(file_path=graph_file_path, output_file="soal/soal", save_to_file=True)

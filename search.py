import json
from Graph import Graph

if __name__ == '__main__':
   print("A* Search for graph")
   graph_file_path: str = 'soal/soal.json'

   with open(graph_file_path) as gf:
        graph_json = json.load(gf)

   start_node: str = graph_json["start"]
   goal_node: str = graph_json["goal"]
   graph: dict = graph_json["graph"]
   heuristic: dict = graph_json["heuristic"]

   graph1 = Graph(graph,heuristic)
   graph1.a_star_algorithm(start_node, goal_node)
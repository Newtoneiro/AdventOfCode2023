import networkx as nx
import os


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")


def main_one():
    g = nx.Graph()  

    with open(filename) as f:
        for line in f.readlines():
            left, right = line.split(":")
            for node in right.strip().split():
                g.add_edge(left, node)
                g.add_edge(node, left)

    g.remove_edges_from(nx.minimum_edge_cut(g))
    a, b = nx.connected_components(g)

    print(len(a) * len(b))


if __name__ == "__main__":  
    main_one()
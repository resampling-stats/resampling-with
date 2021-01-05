import pandas as pd
from mpl_sankey import sankey


import matplotlib.pyplot as plt
import matplotlib


import networkx as nx
import numpy as np

probs = [
    "All Cars", 1,
    [
        "OK", 0.7,
        ["Mechanic ✓", 0.8],
        ["Mechanic ✗", 0.2]
    ],
    [
        "Faulty", 0.3,
        ["Mechanic ✓", 0.1],
        ["Mechanic ✗", 0.9]
    ]
]

def probs_to_graph(p, g=None, parent=None):
    if g is None:
        g = nx.DiGraph()

    node = p[0]
    weight = p[1]
    g.add_node(node)
    if parent:
        g.add_edge(parent, node, weight=weight)

    for prob in p[2:]:
        probs_to_graph(prob, g, parent=node)

    return g

g = probs_to_graph(probs)
root = list(nx.topological_sort(g))[0]
leaves = [x for x in g.nodes() if g.out_degree(x) == 0 and g.in_degree(x) >= 1]

flows = []
for leaf in leaves:
    for path in nx.all_simple_paths(g, root, leaf):
        edges = list(zip(path[:-1], path[1:]))
        weights = [g[a][b]['weight'] for a, b in edges]
        flows.append([
            np.prod(weights),
            *path
        ])

flows = sorted(flows, key=lambda x: x[1:])

plt.figure(figsize=(12, 8))
sankey(flows, cmap=plt.get_cmap('viridis'), titles_color=None)
plt.savefig('sankey.png', bbox_inches='tight')

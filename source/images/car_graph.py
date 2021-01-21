from graphviz import Digraph, nohtml

g = Digraph('g', filename='car_graph.gv',
            graph_attr={'rankdir': 'LR'},
            node_attr={'shape': 'box', 'height': '.1'},
            edge_attr={'arrowsize': '0.5', 'fontsize': '8'})

g.node('All Cars', label='All Cars\n[100]')

g.node('Working Cars', label='Working Cars\n[70]')
g.node('Faulty Cars', label='Faulty Cars\n[30]')

g.node('Faulty Cars, Mechanic OK', label='Mechanic OK\n[3]')
g.node('Faulty Cars, Mechanic Not OK', label='Mechanic Not OK\n[27]')
g.node('Working Cars, Mechanic OK', label='Mechanic OK\n[56]')
g.node('Working Cars, Mechanic Not OK', label='Mechanic Not OK\n[14]')

g.edge('All Cars', 'Working Cars', label='p=0.7')
g.edge('All Cars', 'Faulty Cars', label='p=0.3')
g.edge('Working Cars', 'Working Cars, Mechanic Not OK', label='p=0.2')
g.edge('Working Cars', 'Working Cars, Mechanic OK', label='p=0.8')
g.edge('Faulty Cars', 'Faulty Cars, Mechanic Not OK', label='p=0.9')
g.edge('Faulty Cars', 'Faulty Cars, Mechanic OK', label='p=0.1')

g.view()

from pathlib import Path

import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()

def create_control_flow_graph(previous_node, component, start_y):
    G.add_node(f'If hits {component}', pos=(0, start_y - 1))
    if previous_node is not None:
        G.add_edge(previous_node, f'If hits {component}')

    G.add_node(f'Compute {component} t', pos=(.5, start_y - 2))
    G.add_edge(f'If hits {component}', f'Compute {component} t')

    G.add_node(f'Compute {component} intersect', pos=(.5, start_y - 3))
    G.add_edge(f'Compute {component} t', f'Compute {component} intersect')

    G.add_node(f'If {component} inequality', pos=(.5, start_y - 4))
    G.add_edge(f'Compute {component} intersect', f'If {component} inequality')

    G.add_node(f'Append {component} intersection', pos=(1, start_y - 5))
    G.add_edge(f'If {component} inequality', f'Append {component} intersection')

    G.add_node(f'end {component}', pos=(0, start_y - 6))
    G.add_edge(f'If hits {component}', f'end {component}')
    G.add_edge(f'If {component} inequality', f'end {component}')
    G.add_edge(f'Append {component} intersection', f'end {component}')
    return f'end {component}'


def create_before_graph():
    G.add_node('intersections', pos=(0, 7))
    curr_node = create_control_flow_graph('intersections', 'stem', 6)
    curr_node = create_control_flow_graph(curr_node, 'wing1', -1)
    curr_node = create_control_flow_graph(curr_node, 'wing2', -8)
    G.add_node('return intersections', pos=(0, -16))
    G.add_edge(curr_node, 'return intersections')

    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos)
    outfile = Path(__file__).parent / 'complexity1.png'
    plt.savefig(str(outfile), figsize=(1, 5))


def create_after_graph():
    G.add_node('main', pos=(0, 7))
    create_control_flow_graph(None, 'stem', 6)
    create_control_flow_graph(None, 'wing1', -1)
    create_control_flow_graph(None, 'wing2', -8)
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos)
    outfile = Path(__file__).parent / 'complexity2.png'
    plt.savefig(str(outfile), figsize=(1, 5))


G.clear()
create_before_graph()

G.clear()
create_after_graph()

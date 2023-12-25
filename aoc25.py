import networkx as nx
raw_input = []
f = open('aoc25.txt','rt')
for line in f:
    raw_input += [line[:-1]]
f.close()
G = nx.Graph()
for line in raw_input:
    node1, remaining = line.split(': ')
    remaining_nodes = remaining.split(' ')
    for node in remaining_nodes:
        G.add_edge(node1, node)
edges_to_cut = nx.minimum_edge_cut(G)
for edge in edges_to_cut:
    G.remove_edge(edge[0], edge[1])
remaining_groups = list(nx.connected_components(G))
answer = len(remaining_groups[0]) * len(remaining_groups[1])
print('Part 1: ' + str(answer))
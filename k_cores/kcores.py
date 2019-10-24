from k_cores.MyHeap import MyHeap

input_filename = 'example_graph.txt'

if __name__ == '__main__':
    g = {}

    with open(input_filename) as graph_input:
        for line in graph_input:
            # Split line and convert line parts to integers.
            nodes = [int(x) for x in line.split()]
            if len(nodes) != 2:
                continue
            # If a node is not already in the graph
            # we must create a new empty list.
            if nodes[0] not in g:
                g[nodes[0]] = []
            if nodes[1] not in g:
                g[nodes[1]] = []
            # We need to append the "to" node
            # to the existing list for the "from" node.
            g[nodes[0]].append(nodes[1])
            # And also the other way round.
            g[nodes[1]].append(nodes[0])

    V_size = len(g)
    mh = MyHeap()
    d = [0] * V_size
    p = [0] * V_size
    core = [0] * V_size

    for v in range(0, V_size):
        d[v] = len(g[v])
        p[v] = len(g[v])
        mh.insert_in_pq([p[v], v])

    while len(mh) > 0:
        t = mh.extract_min_from_pq()
        core[t[1]] = t[0]
        if len(mh) != 0:
            for v in g[t[1]]:
                d[v] -= 1
                opn = [p[v], v]
                p[v] = max(t[0], d[v])
                npn = [p[v], v]
                mh.replace(opn, npn)

    with open('result.txt', 'w') as out:
        i = 0
        for value in core:
            line = str(i) + " " + str(value) + '\n'
            out.writelines(line)
            i += 1

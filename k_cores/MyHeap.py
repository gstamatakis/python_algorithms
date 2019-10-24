class MyHeap:
    def __init__(self):
        self.pq = []

    def __len__(self):
        return len(self.pq)

    def add_last(self, c):
        self.pq.append(c)

    def root(self):
        return 0

    def set_root(self, c):
        if len(self.pq) != 0:
            self.pq[0] = c

    # The 'key' of each heap node is the potential core number which
    # is located in the first cell of each dictionary entry.
    def get_data(self, p):
        return self.pq[p][0]

    def children(self, p):
        if 2 * p + 2 < len(self.pq):
            return [2 * p + 1, 2 * p + 2]
        else:
            return [2 * p + 1]

    def parent(self, p):
        return (p - 1) // 2

    def exchange(self, p1, p2):
        self.pq[p1], self.pq[p2] = self.pq[p2], self.pq[p1]

    def insert_in_pq(self, c):
        self.add_last(c)
        i = len(self.pq) - 1
        while i != self.root() and self.get_data(i) < self.get_data(self.parent(i)):
            p = self.parent(i)
            self.exchange(i, p)
            i = p

    def extract_last_from_pq(self):
        return self.pq.pop()

    def has_children(self, p):
        return 2 * p + 1 < len(self.pq)

    def extract_min_from_pq(self):
        c = self.pq[self.root()]
        self.set_root(self.extract_last_from_pq())
        i = self.root()
        while self.has_children(i):
            # Use the data stored at each child as the comparison key
            # for finding the minimum.
            j = min(self.children(i), key=lambda x: self.get_data(x))
            if self.get_data(i) < self.get_data(j):
                return c
            self.exchange(i, j)
            i = j
        return c

    # Replaces a node of a heap with another node
    def replace(self, opn, npn):
        # Old and new nodes are the same. No need to update.
        if opn == npn:
            return

        # If old isn't in the heap we can't update it.
        if opn not in self.pq:
            return

        # Search for the node to replace.
        line_number = 0
        for core, node in self.pq:
            if node == opn[1]:
                self.pq[line_number] = npn

                # When the node is found we also need to send the smaller node towards the root.
                i = line_number
                while i != self.root() and self.get_data(i) < self.get_data(self.parent(i)):
                    p = self.parent(i)
                    self.exchange(i, p)
                    i = p

                return
            line_number += 1

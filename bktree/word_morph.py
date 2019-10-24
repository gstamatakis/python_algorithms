import sys
import editdistance
from collections import deque


# Algorithm 2
# Each node consists of a string (the word) and a children dictionary of [distance,word] pairs
def tree_insertion(tree, word):
    if len(tree) == 0:
        tree.append([word, {}])
        return
    node = tree[0]
    while node is not None:
        node_word = node[0]
        distance = editdistance.distance(word, node_word)
        parent = node
        node = node[1].get(distance)
        if not node:
            parent[1][distance] = [word, {}]


# Algorithm 3
# Insert a word to the BK tree. We will try to insert each word as a child of a similar word.
def bk_search(tree, word, r):
    results = []
    to_check = deque()
    to_check.append(tree[0])
    while to_check:
        node_word, children = to_check.pop()
        distance = editdistance.distance(word, node_word)
        if distance <= r:
            results.append([distance, node_word])
        l, h = distance - r, distance + r
        if len(children) == 0:
            continue
        # From the python documentation:
        # extend(iterable):
        #   Extends the right side of the deque by appending elements from the iterable argument.
        to_check.extend(c for d, c in children.items() if l <= d <= h)
    return results


# Finds the min element of an array AND a set.
def find_min(a, openset):
    min_index = -1
    min_val = sys.maxsize
    for (i, v) in a.items():
        if v < min_val and i in openset:
            min_index = i
            min_val = v
    return min_index


# Source: https://en.wikipedia.org/wiki/A*_search_algorithm
def A_star_search(tree, source_word, goal_word):
    # The set of nodes already evaluated
    closedSet = set()

    # The set of currently discovered nodes that are not evaluated yet.
    # Initially, only the start node is known.
    openSet = set()
    openSet.add(source_word)

    # For each node, which node it can most efficiently be reached from.
    # If a node can be reached from many nodes, cameFrom will eventually contain the
    # most efficient previous step.
    cameFrom = {}

    # For each node, the cost of getting from the start node to that node.
    # The cost of going from start to start is zero.
    gScore = {source_word: 0}

    # For each node, the total cost of getting from the start node to the goal
    # by passing by that node. That value is partly known, partly heuristic.
    # For the first node, that value is completely heuristic.
    fScore = {source_word: editdistance.distance(source_word, goal_word)}

    while openSet:
        current = find_min(fScore, openSet)  # Find the word with fmin AND in openset

        # If this word is the one we are looking for then return the reconstructed path
        if current == goal_word:
            return reconstruct_path(cameFrom, current)

        # Update the open/closed sets
        openSet.remove(current)
        closedSet.add(current)

        for new_node in bk_search(tree, current, 1):
            neighbour = new_node[1]
            if neighbour in closedSet:  # Ignore the neighbor which is already evaluated.
                continue
            # The distance from start to a neighbor
            tentative_gScore = gScore.get(current, sys.maxsize) + editdistance.distance(current, neighbour)

            if neighbour not in openSet:  # Discover a new node
                openSet.add(neighbour)
            elif tentative_gScore >= gScore.get(neighbour, sys.maxsize):  # Not a better path
                continue

            # This path is the best until now. Record it!
            cameFrom[neighbour] = current
            gScore[neighbour] = tentative_gScore
            fScore[neighbour] = gScore.get(neighbour) + editdistance.distance(neighbour, goal_word)

    # If we cant find a path between these 2 words then return that contains only the source word
    return reconstruct_path(cameFrom, source_word)


# Creates the path from the current node to the source node
# The path is created by appending the parent of each node to a list and
# then jumping instantly to the parent
def reconstruct_path(cameFrom, current):
    total_path = [current]
    while current in cameFrom.keys():
        current = cameFrom[current]
        total_path.append(current)
    return total_path


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Need 3 arguments!')
        exit(-1)

    start = sys.argv[2]
    target = sys.argv[3]

    # The BK Tree. Read the file and put each word in the tree
    bk_tree = []
    with open(sys.argv[1], 'r') as f:
        for line in f:
            tree_insertion(bk_tree, line[:-1])  # Discard newline

    # Find the smallest path between 2 words
    path = A_star_search(bk_tree, start, target)
    for word in reversed(path):
        print(word, end=' ')
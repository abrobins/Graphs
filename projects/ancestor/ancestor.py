class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


# builds graph dictionary with child and parents

def earliest_ancestor(ancestors, starting_node):
    graph = {}
    q = Queue()
    visited_verts = set()
    longest_path = 1
    earliest_ancestor = -1


# get working with graph & add ancestor
    for p in ancestors:
        graph[p[1]] = set()
    for p in ancestors:
        graph[p[1]].add(p[0])

    if starting_node not in graph:
        return -1

    q.enqueue([starting_node])

    while q.size() > 0:
        curr_path = q.dequeue()
        curr_node = curr_path[-1]

        if curr_node not in visited_verts:
            visited_verts.add(curr_node)
            neighbors = graph.get(curr_node)
            if neighbors is not None:
                for neighbor in neighbors:
                    new_path = curr_path + [neighbor]
                    q.enqueue(new_path)
            else:
                if len(curr_path) > longest_path or (len(curr_path) == longest_path and curr_node < earliest_ancestor):
                    longest_path = len(curr_path)
                    earliest_ancestor = curr_node

    return earliest_ancestor

"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {
            # 1: {2},
            # 2: {3, 4},
            # 3: {5},  represents example graph from lecture
            # 4: {6, 7},
            # 5: {3},
            # 6: {3},
            # 7: {1, 6}
        }

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # Create new key with vertex id and set value to empty set (meaning no edges yet)
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # Find vertex v1 in our vertices, add v2 to set of edges
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue and enqueue the starting_vertex
        q = Queue()
        q.enqueue(starting_vertex)
        # create an empty set to track visited vertices
        visited_vertices = set()
        # while the queue is not empty:
        while q.size() > 0:
            current_node = q.dequeue()
            # get current vertex (dequeue from queue)

        # check if the current vertex has not been visited
            if current_node not in visited_vertices:
                visited_vertices.add(current_node)
                print(current_node)
                neighbors = self.get_neighbors(current_node)

                for neighbor in neighbors:
                    q.enqueue(neighbor)
            # print the current vertex
            # mark current vertex as visited
                # add the current vertex to a visited_set

            # queue up all current vertices' neighbors so we can visit them next (can use get_neighbors function)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        # create an empty stack and add the starting_vertex
        # create an empty set to track visited vertices
        s = Stack()
        s.push(starting_vertex)
        visited_vertices = set()

        # while the stack is not empty:
        while s.size() > 0:
            current_node = s.pop()
        # get current vertex (pop from stack)

        # check if the current vertex has not been visited
            if current_node not in visited_vertices:
                visited_vertices.add(current_node)
                print(current_node)
                neighbors = self.get_neighbors(current_node)

                for neighbor in neighbors:
                    s.push(neighbor)

        # print the current vertex
        # mark current vertex as visited
        # add the current vertex to a visited_set

        # push up all current vertices' neighbors so we can visit them next (can use get_neighbors function)

        pass  # TODO

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.





        # check if the current vertex has not been visited
            # CHECK IF CURRENT VERTEX IS DESTINATION
            # IF IT IS STOP AND RETURN

            # mark current vertex as visited
                # add the current vertex to a visited_set




        """
        # create an empty queue and enqueue PATH to the starting_vertex
        # create an empty set to track visited vertices
        q = Queue()  # key component of BFS
        visited_vertices = set()  # key component of BFS
        q.enqueue([starting_vertex])  # key component of BFS
        # while the queue is not empty:
        # get current vertex PATH (dequeue from queue)
        # set current vertex to last element of the path
        while q.size() > 0:
            current_path = q.dequeue()
            last_vertex = current_path[-1]
            if last_vertex == destination_vertex:
                return current_path
            if last_vertex not in visited_vertices:  # if you don't do this you could end up in loop
                visited_vertices.add(last_vertex)

                # Queue up new paths with each neighbor
                # take current path
                # append neighbor to it
                # queue up new path
                for neighbor in self.get_neighbors(last_vertex):
                    new_path = current_path + [neighbor]
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        visited_vertices = set()
        s.push([starting_vertex])
        while s.size() > 0:
            current_path = s.pop()
            last_vertex = current_path[-1]
            if last_vertex == destination_vertex:
                return current_path
            if last_vertex not in visited_vertices:
                visited_vertices.add(last_vertex)

                for neighbor in self.get_neighbors(last_vertex):
                    new_path = current_path + [neighbor]
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        if visited is None:
            visited = set()

        if path is None:
            path = []

        if starting_vertex not in visited:
            visited.add(starting_vertex)

            # copy path so you don't have to change original path

            copy_path = path.copy()
            copy_path.append(starting_vertex)

            if starting_vertex == destination_vertex:
                return copy_path

            for neighbor in self.get_neighbors(starting_vertex):
                new_path = self.dfs_recursive(
                    neighbor, destination_vertex, visited, copy_path)

                if new_path is not None:
                    return new_path

        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))

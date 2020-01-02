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

def bfs(player, starting_vertex, destination_vertex,player_graph):
    """
    Return a list containing the shortest path from
    starting_vertex to destination_vertex in
    breath-first order.
    """
    q = Queue()
    q.enqueue( [starting_vertex])
    visited = set()
 
    while q.size() >0:
        path = q.dequeue()
        v = path[-1]
        if v not in visited:
            if v == destination_vertex:
                return path
            visited.add(v)
            for direction in player_graph[v].keys():
                if direction in ["n","w","e","s"]:
                    path_copy = path.copy()
                    dd=player_graph[v][direction]
                    if dd == "?":
                        pass
                    else:
                        path_copy.append(dd)
                        q.enqueue(path_copy)
                else:
                    break

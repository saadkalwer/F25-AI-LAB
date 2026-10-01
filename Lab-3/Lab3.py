# AI Lab 3 - Saad Ahmed (009)
from collections import deque
import heapq

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}

def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = []
    while queue:
        node, path = queue.popleft()
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path, visited
        for child in graph[node]:
            queue.append((child, path + [child]))
    return None, visited

def dfs(start, goal):
    stack = [(start, [start])]
    visited = []
    while stack:
        node, path = stack.pop()
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path, visited
        for child in reversed(graph[node]):
            stack.append((child, path + [child]))
    return None, visited

def dls(node, goal, limit, path=None):
    if path is None:
        path = [node]
    if node == goal:
        return "FOUND", path
    if limit == 0:
        return "CUTOFF", None
    cutoff_happened = False
    for child in graph[node]:
        if child not in path:
            status, result = dls(child, goal, limit - 1, path + [child])
            if status == "FOUND":
                return status, result
            if status == "CUTOFF":
                cutoff_happened = True
    if cutoff_happened:
        return "CUTOFF", None
    return "FAILURE", None

def iddfs(start, goal, maximum_depth):
    for limit in range(maximum_depth + 1):
        status, path = dls(start, goal, limit)
        print("  Tried limit", limit, "->", status)
        if status == "FOUND":
            return status, path
    return "CUTOFF", None

weighted_graph = {
    "A": [("B", 1), ("C", 2)],
    "B": [("D", 4), ("E", 1)],
    "C": [("F", 2), ("G", 10)],
    "D": [],
    "E": [("G", 1)],
    "F": [],
    "G": []
}

def ucs(start, goal):
    queue = [(0, start, [start])]
    visited = []
    while queue:
        cost, node, path = heapq.heappop(queue)
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path, cost, visited
        for child, edge_cost in weighted_graph[node]:
            heapq.heappush(queue, (cost + edge_cost, child, path + [child]))
    return None, None, visited

print("BFS:", bfs("A", "G"))
print("DFS:", dfs("A", "G"))

for limit in [1, 2, 3, 4]:
    print("DLS limit", limit, ":", dls("A", "G", limit))

for maximum in [1, 2, 3, 4]:
    print("IDDFS maximum", maximum)
    print(iddfs("A", "G", maximum))

print("UCS:", ucs("A", "G"))
print("BFS uses fewer edges on the weighted graph: A -> C -> G, cost = 12")
print("UCS finds the cheaper route: A -> B -> E -> G, cost = 3")

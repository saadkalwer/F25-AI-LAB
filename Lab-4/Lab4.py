from heapq import heappush, heappop
from itertools import count

# Weighted campus graph. Neighbours are kept in the stated successor order.
GRAPH = {
    "S": [("A", 2), ("B", 4)],
    "A": [("S", 2), ("C", 2), ("D", 5)],
    "B": [("S", 4), ("D", 1), ("E", 4)],
    "C": [("A", 2), ("D", 1), ("G", 7)],
    "D": [("A", 5), ("B", 1), ("C", 1), ("E", 2), ("G", 5)],
    "E": [("B", 4), ("D", 2), ("G", 2)],
    "G": [("C", 7), ("D", 5), ("E", 2)],
}

HEURISTIC = {"S": 7, "A": 6, "B": 5, "C": 5, "D": 4, "E": 2, "G": 0}

def search(heuristic):
    order = count()
    frontier = [(heuristic["S"], next(order), "S")]
    best_g = {"S": 0}
    parent = {"S": None}
    expanded = []

    while frontier:
        queued_f, _, node = heappop(frontier)
        g = best_g[node]
        if queued_f != g + heuristic[node]:
            continue
        expanded.append((node, g, heuristic[node], g + heuristic[node]))
        if node == "G":
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return list(reversed(path)), g, expanded
        for neighbour, cost in GRAPH[node]:
            new_g = g + cost
            if new_g < best_g.get(neighbour, float("inf")):
                best_g[neighbour] = new_g
                parent[neighbour] = node
                heappush(frontier, (new_g + heuristic[neighbour], next(order), neighbour))
    return None, float("inf"), expanded

def show_run(label, heuristic):
    path, cost, expanded = search(heuristic)
    print(f"\n{label}")
    print("Path:", " -> ".join(path))
    print("Cost:", cost)
    print("Expanded:", [row[0] for row in expanded])
    print("Count:", len(expanded))
    print("Trace (node, g, h, f):")
    for row in expanded:
        print(row)
    return path, cost, expanded

if __name__ == "__main__":
    print("First three A* expansions:")
    normal = search(HEURISTIC)
    for row in normal[2][:3]:
        print(row)
    show_run("A* with supplied heuristic", HEURISTIC)
    show_run("UCS control (h = 0)", {node: 0 for node in GRAPH})
    changed = HEURISTIC.copy()
    changed["C"] = 10
    show_run("A* after changing h(C) from 5 to 10", changed)

from collections import deque

# BFS Implementation
def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])
    while queue:
        current, path = queue.popleft()
        if current == goal:
             return path
        visited.add(current)
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)
    return None

# DFS Implementation
def dfs(graph, start, goal):
    visited = set()
    stack = [(start, [start])]
    while stack:
        current, path = stack.pop()
        if current == goal:
            return path
        visited.add(current)
        for neighbor in reversed(graph.get(current, [])):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
                visited.add(neighbor)
    return None

# Read Graph from User
def read_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))
    for _ in range(num_nodes):
        node = input("Enter node name: ")
        neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
        graph[node] = neighbors
    return graph

# Main Program
def main():
    print("State Space Search: BFS or DFS")
    graph = read_graph()
    
    start = input("Enter the start state: ")
    goal = input("Enter the goal state: ")
    
    algo = input("Choose algorithm (BFS/DFS): ").strip().lower()

    if algo == 'bfs':
        path = bfs(graph, start, goal)
    elif algo == 'dfs':
        path = dfs(graph, start, goal)
    else:
        print("Invalid algorithm choice.")
        return

    if path:
        print("Path found:", " -> ".join(path))
    else:
        print("No path found.")

if __name__ == "__main__":
    main()

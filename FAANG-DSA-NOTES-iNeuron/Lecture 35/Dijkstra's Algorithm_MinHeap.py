import heapq

## Dijkstra's Algorithm
def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found.
            ## Relaxation of Edges
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

## storage of the graph is done via adjacency list
distances = {
    'A': {'B': 2, 'C': 5, 'D': 2, 'E': 7, 'F': 50},
    'B': {'C': 2, 'D': 1, 'E': 2, 'F':60},
    'C': {'B': 3, 'E': 2, 'F': 90},
    'D': {'E': 1, 'F': 3},
    'E': {'D': 4, 'F': 4},
    'F': {}}

print(calculate_distances(distances, 'A'))
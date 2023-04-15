mport heapq
def dijkstra(graph, start):
distances = {node: float('inf') for node in graph}
distances[start] = 0
heap = [(0, start)]
while heap:
(current_distance, current_node) = heapq.heappop(heap)
if current_distance > distances[current_node]:
continue
for neighbor, weight in graph[current_node].items():
distance = current_distance + weight
if distance < distances[neighbor]:
distances[neighbor] = distance
heapq.heappush(heap, (distance, neighbor))
DIST
1
2
0
4
8
Inf
DIST
inf
inf
inf
6
inf
0return distances
graph = {
'A': {'B': 5, 'C': 1},
'B': {'A': 5, 'C': 2, 'D': 1},
'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
'E': {'C': 8, 'D': 3},
'F': {'D': 6}
}
start = 'A'
distances = dijkstra(graph, start)
for node in distances:
print(f'Distance from NODE {start} to NODE {node}: {distances[node]}')

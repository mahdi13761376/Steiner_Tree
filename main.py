f = open("steiner_in.txt", "r")
steiner_vertices_number, terminal_vertices_number, edge_numbers = f.readline().split()
steiner_vertices_number = int(steiner_vertices_number)
terminal_vertices_number = int(terminal_vertices_number)
edge_numbers = int(edge_numbers)
vertices_number = steiner_vertices_number + terminal_vertices_number
print(steiner_vertices_number, terminal_vertices_number, edge_numbers)
i = 0
vertices = []
for i in range(0, steiner_vertices_number):
    line = f.readline()
    vertices.append(line.split())
for i in range(0, terminal_vertices_number):
    line = f.readline()
    vertices.append(line.split())
graph = [[0 for x in range(vertices_number)] for y in range(vertices_number)]
for i in range(0, edge_numbers):
    line = f.readline()
    edge1, edge2 = line.split()
    edge1 = int(edge1)
    edge2 = int(edge2)
    x_edge1, y_edge_1 = [int(x) for x in vertices[edge1]]
    x_edge2, y_edge_2 = [int(x) for x in vertices[edge2]]
    distance = pow(pow(x_edge1 - x_edge2, 2) + pow(y_edge_1 - y_edge_2, 2), 0.5)
    graph[edge1][edge2] = distance
    graph[edge2][edge1] = distance
print(graph)

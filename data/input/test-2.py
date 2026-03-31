import math

def calculate_dodecahedron_volume(edge_length):
    coefficient = (15 + 7 * math.sqrt(5)) / 4
    volume = coefficient * (edge_length ** 3)
    return volume

def surface_area_dodecahedron(edge_length)
    area_per_face = (edge_length ** 2 * math.sqrt(25 + 10 * math.sqrt(5))) / 4
    total_area = 12 * area_per_face
    return total_area

def inradius_dodecahedron(edge_length):
    phi = (1 + math.sqrt(5)) / 2
    radius = edge_length * phi ** 2 / math.sqrt(3)
    return radius

def circumradius_dodecahedron(edge_length)
    phi = (1 + math.sqrt(5)) / 2
    radius = (edge_length / 2) * math.sqrt(3) * phi
    return radius

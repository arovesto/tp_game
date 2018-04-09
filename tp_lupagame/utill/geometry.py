def distance(a, b):
    return sum((a[i] - b[i]) ** 2 for i in range(len(a))) ** 0.5


def can_move_to(chunk):
    return lambda position: position in chunk and chunk[position].walkable


class Circle:
    def __init__(self, radius, center=(0, 0)):
        self.radius = radius
        self.points = {(center[0] + i, center[1] + j) for i in range(-radius, radius + 1) for j in range(-radius, radius + 1) if distance((i, j), (0, 0)) <= radius }

    def __getitem__(self, item):
        return self.points[item]
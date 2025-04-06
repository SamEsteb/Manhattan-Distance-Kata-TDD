class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def manhattan_distance(point1, point2):
    return abs(point1.x - point2.x) + abs(point1.y - point2.y)
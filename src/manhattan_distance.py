class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def manhattan_distance(point1, point2):
    diff_x = abs(point1.x - point2.x)
    diff_y = point1.y - point2.y
    if diff_y < 0:
        diff_y = -diff_y
    return diff_x + diff_y
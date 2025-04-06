class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def manhattan_distance(point1, point2):
    diff_x = point1.x - point2.x
    if diff_x < 0:
        diff_x = -diff_x
    return diff_x
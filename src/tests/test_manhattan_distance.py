import pytest
from src.manhattan_distance import Point, manhattan_distance

def test_manhattan_distance_2_puntos_iguales():
    point1 = Point(1, 2)
    point2 = Point(1, 2)
    assert manhattan_distance(point1, point2) == 0

def test_manhattan_distance_2_puntos_distintos_eje_X_punto1x_mayor_punto2x():
    point1 = Point(9, 0)
    point2 = Point(5, 0)
    assert manhattan_distance(point1, point2) == 4
import pytest
from src.manhattan_distance import Point, manhattan_distance

def test1_manhattan_distance_2_puntos_iguales():
    point1 = Point(1, 2)
    point2 = Point(1, 2)
    assert manhattan_distance(point1, point2) == 0

def test2_manhattan_distance_2_puntos_distintos_eje_X_punto1x_mayor_punto2x():
    point1 = Point(9, 0)
    point2 = Point(5, 0)
    assert manhattan_distance(point1, point2) == 4

def test3_manhattan_distance_2_puntos_distintos_eje_X_punto1x_menor_punto2x():
    point1 = Point(5, 0)
    point2 = Point(9, 0)
    assert manhattan_distance(point1, point2) == 4

def test4_manhattan_distance_2_puntos_distintos_eje_Y_punto1y_mayor_punto2y():
    point1 = Point(0, 12)
    point2 = Point(0, 4)
    assert manhattan_distance(point1, point2) == 8

def test5_manhattan_distance_2_puntos_distintos_eje_Y_punto1y_menor_punto2y():
    point1 = Point(0, 4)
    point2 = Point(0, 12)
    assert manhattan_distance(point1, point2) == 8

def test6_1_manhattan_distance_eje_X_distinto_eje_Y_igual():
    point1 = Point(2, 3)
    point2 = Point(5, 3)
    assert manhattan_distance(point1, point2) == 3

def test6_2_manhattan_distance_eje_X_igual_eje_Y_distinto():
    point1 = Point(2, 3)
    point2 = Point(2, 5)
    assert manhattan_distance(point1, point2) == 2

def test6_3_manhattan_distance_eje_X_distinto_eje_Y_distinto():
    point1 = Point(2, 3)
    point2 = Point(5, 5)
    assert manhattan_distance(point1, point2) == 5

def test6_4_manhattan_distance_eje_X_distinto_eje_Y_igual_invertido():
    point1 = Point(5, 3)
    point2 = Point(2, 3)
    assert manhattan_distance(point1, point2) == 3

def test6_5_manhattan_distance_eje_X_igual_eje_Y_distinto_invertido():
    point1 = Point(2, 5)
    point2 = Point(2, 3)
    assert manhattan_distance(point1, point2) == 2

def test6_6_manhattan_distance_eje_X_distinto_eje_Y_distinto_invertido():
    point1 = Point(5, 5)
    point2 = Point(2, 3)
    assert manhattan_distance(point1, point2) == 5

def test7_manhattan_distance_2_puntos_distintos_ejes_negativos():
    # caso 1: Negativo en eje X, el resto 0
    assert manhattan_distance(Point(-5, 0), Point(0, 0)) == 5
    # caso 2: Negativo en eje Y, el resto 0
    assert manhattan_distance(Point(0, -5), Point(0, 0)) == 5
    # caso 3: punto1 negativo en eje X y Y, punto 2 positivo
    assert manhattan_distance(Point(-5, -6), Point(2, 2)) == 15
    # caso 4: punto1 positivo en eje X y Y, punto 2 negativo
    assert manhattan_distance(Point(5, 7), Point(-2, -2)) == 16
    # caso 5: punto1 negativo en eje X positivo en eje Y, punto 2 positivo en eje X negativo en eje Y
    assert manhattan_distance(Point(-5, 6), Point(2, -2)) == 15
    # caso 6: punto1 positivo en eje X negativo en eje Y, punto 2 negativo en eje X positivo en eje Y
    assert manhattan_distance(Point(5, -8), Point(-2, 2)) == 17
    # caso 7: Ambos puntos negativos en eje X y Y
    assert manhattan_distance(Point(-5, -6), Point(-2, -2)) == 7
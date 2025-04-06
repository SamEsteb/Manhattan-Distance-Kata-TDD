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

def test6_manhattan_distance_2_puntos_distintos_ambos_ejes():
    # caso 1: Eje X distinto y Eje Y igual
    assert manhattan_distance(Point(2,3), Point(5,3)) == 3
    # caso 2: Eje X igual y Eje Y distinto
    assert manhattan_distance(Point(2,3), Point(2,5)) == 2
    # caso 3: Eje X distinto y Eje Y distinto
    assert manhattan_distance(Point(2,3), Point(5,5)) == 5

    # caso 4: Eje X distinto y Eje Y igual (puntos invertidos)
    assert manhattan_distance(Point(5,3), Point(2,3)) == 3
    # caso 5: Eje X igual y Eje Y distinto (puntos invertidos)
    assert manhattan_distance(Point(2,5), Point(2,3)) == 2
    # caso 6: Eje X distinto y Eje Y distinto (puntos invertidos)
    assert manhattan_distance(Point(5,5), Point(2,3)) == 5

    
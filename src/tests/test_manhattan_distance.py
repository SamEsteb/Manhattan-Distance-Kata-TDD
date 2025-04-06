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

# Casos 7_1 y 7_2: son para verificar que el valor absoluto funciona correctamente
def test7_1_manhattan_distance_negativo_en_eje_X_resto_0():
    point1 = Point(-5, 0)
    point2 = Point(0, 0)
    assert manhattan_distance(point1, point2) == 5

def test7_2_manhattan_distance_negativo_en_eje_Y_resto_0():
    point1 = Point(0, -5)
    point2 = Point(0, 0)
    assert manhattan_distance(point1, point2) == 5

def test7_3_manhattan_distance_punto1_negativo_punto2_positivo():
    point1 = Point(-5, -6)
    point2 = Point(2, 2)
    assert manhattan_distance(point1, point2) == 15

def test7_4_manhattan_distance_punto1_positivo_punto2_negativo():
    point1 = Point(5, 7)
    point2 = Point(-2, -2)
    assert manhattan_distance(point1, point2) == 16

def test7_5_manhattan_distance_punto1_negativo_X_punto2_negativo_Y():
    point1 = Point(-5, 6)
    point2 = Point(2, -2)
    assert manhattan_distance(point1, point2) == 15

def test7_6_manhattan_distance_punto1_negativo_Y_punto2_negativo_X():
    point1 = Point(5, -8)
    point2 = Point(-2, 2)
    assert manhattan_distance(point1, point2) == 17

def test7_7_manhattan_distance_ambos_puntos_negativos():
    point1 = Point(-5, -6)
    point2 = Point(-2, -2)
    assert manhattan_distance(point1, point2) == 7
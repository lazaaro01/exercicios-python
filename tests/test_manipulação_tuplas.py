import pytest
from aula3.manipulação_tuplas import unir_tuplas, extrair_info, ordenar_tuplas, multiplicar_tuplas

def test_unir_tuplas():
    assert unir_tuplas((1, 2), (3, 4)) == (1, 2, 3, 4)
    assert unir_tuplas((), (3, 4)) == (3, 4)
    assert unir_tuplas((1, 2), ()) == (1, 2)
    assert unir_tuplas((), ()) == ()

def test_extrair_info():
    assert extrair_info((('nome', 'João'), ('idade', 25))) == {'nome': 'João', 'idade': 25}
    assert extrair_info((('cidade', 'São Paulo'), ('populacao', 123456))) == {'cidade': 'São Paulo', 'populacao': 123456}

def test_ordenar_tuplas():
    assert ordenar_tuplas([('a', 3), ('b', 1), ('c', 2)]) == [('b', 1), ('c', 2), ('a', 3)]
    assert ordenar_tuplas([('x', 5), ('y', 2), ('z', 2)]) == [('y', 2), ('z', 2), ('x', 5)]
    assert ordenar_tuplas([('a', 1), ('b', 1), ('c', 1)]) == [('a', 1), ('b', 1), ('c', 1)]

def test_multiplicar_tuplas():
    assert multiplicar_tuplas((1, 2, 3), (4, 5, 6)) == (4, 10, 18)
    assert multiplicar_tuplas((2, 3), (4, 5)) == (8, 15)
    assert multiplicar_tuplas((1, 2), ()) == ()

def unir_tuplas(tupla1, tupla2):
    """Une duas tuplas, mantendo a ordem da primeira e adicionando os elementos da segunda."""
    return tupla1 + tupla2

def extrair_info(tuplas):
    """Converte uma tupla de tuplas em um dicionário."""
    return dict(tuplas)

def ordenar_tuplas(tuplas):
    """Ordena uma lista de tuplas com base no valor."""
    return sorted(tuplas, key=lambda x: x[1])

def multiplicar_tuplas(tupla1, tupla2):
    """Multiplica os valores correspondentes de duas tuplas."""
    return tuple(a * b for a, b in zip(tupla1, tupla2))

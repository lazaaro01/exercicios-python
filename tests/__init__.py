import pytest

@pytest.fixture(scope="module")
def exemplo_fixture():
    return {"nome": "João", "idade": 25}

import dojo

def test_moedas_1():
    (notas, moedas) = dojo.moedas(1)
    assert notas == [0, 0, 0, 0, 0, 0]
    assert moedas == [1, 0, 0, 0, 0, 0]

def test_moedas_050():
    (notas, moedas) = dojo.moedas(0.5)
    assert notas == [0, 0, 0, 0, 0, 0]
    assert moedas == [0, 1, 0, 0, 0, 0]

def test_moedas_150():
    (notas, moedas) = dojo.moedas(1.5)
    assert notas == [0, 0, 0, 0, 0, 0]
    assert moedas == [1, 1, 0, 0, 0, 0]

def test_moedas_191():
    (notas, moedas) = dojo.moedas(1.91)
    assert notas == [0, 0, 0, 0, 0, 0]
    assert moedas == [1, 1, 1, 1, 1, 1]

def test_moedas_192():
    (notas, moedas) = dojo.moedas(1.92)
    assert notas == [0, 0, 0, 0, 0, 0]
    assert moedas == [1, 1, 1, 1, 1, 2]

def test_notas_100():
    (notas, moedas) = dojo.moedas(100)
    assert notas == [1, 0, 0, 0, 0, 0]
    assert moedas == [0, 0, 0, 0, 0, 0]

def test_notas_101():
    (notas, moedas) = dojo.moedas(101)
    assert notas == [1, 0, 0, 0, 0, 0]
    assert moedas == [1, 0, 0, 0, 0, 0]

def test_notas_101_92():
    (notas, moedas) = dojo.moedas(101.92)
    assert notas == [1, 0, 0, 0, 0, 0]
    assert moedas == [1, 1, 1, 1, 1, 2]

def test_notas_576_73():
    (notas, moedas) = dojo.moedas(576.73)
    assert notas == [5, 1, 1, 0, 1, 0]
    assert moedas == [1, 1, 0, 2, 0, 3]

def test_notas_0():
    (notas, moedas) = dojo.moedas(0.0)
    assert notas == [0, 0, 0, 0, 0, 0]
    assert moedas == [0, 0, 0, 0, 0, 0]

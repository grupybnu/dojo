from main import unica_chance

def test_case_basico():
    assert unica_chance('AAD')
    assert unica_chance('AAA')
    assert unica_chance('ABDC')
    assert unica_chance('ZBCDEFGHIJKLMNOPQRSTUVWXYA')

def test_case_basico_falha():
    assert not unica_chance('AACDB')
    assert not unica_chance('ACDB')
    assert not unica_chance('ABCDFGHIEJ')
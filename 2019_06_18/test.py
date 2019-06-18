import pytest

from main import solucao


@pytest.mark.parametrize('texto,saida', [
    ('x', ['x:x']),
    ('xzy', ['x:z']),
    ('aha', ['a:a', 'h:h']),
    ('fbxeac', ['a:c', 'e:f', 'x:x']),
    ('quick brown fox jumps over the lazy dog', ['a:z']),
    ('  b z a x c y', ['a:c', 'x:z']),
    ('bdfhjlnprtvxz', ['b:b', 'd:d', 'f:f', 'h:h', 'j:j', 'l:l', 'n:n', 'p:p', 'r:r', 't:t', 'v:v', 'x:x', 'z:z'])
])
def test(texto, saida):
    assert solucao(texto) == saida
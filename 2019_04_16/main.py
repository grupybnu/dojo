# Problema: A Única Chance
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2496

def unica_chance(in_str):
    l = zip(in_str, sorted(in_str))
    l = map(lambda x: x[0] != x[1], l)
    l = filter(None, l)
    return len(list(l)) <= 2


# após resolver o problema com a função acima
# decidimos dedicar um tempo para encontrar uma solução melhor
# a função abaixo foi uma tentativa, mas não deu muito certo :b
# você tem alguma outra ideia?
def unica_chance_2(in_str):
    print('========')
    maior = 'A'
    for (i, j) in zip(in_str[:-1], in_str[1:]):
        print(i, j)
        if i <= j:
            maior = i
        elif j < maior:
            return False
    
    return True

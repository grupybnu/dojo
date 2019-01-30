# Problema: Notas e Moedas
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1021

MOEDAS = [1, 0.5, 0.25, 0.1, 0.05, 0.01]
NOTAS = [100, 50, 20, 10, 5, 2]

def moedas(valor):
    notas = [0, 0, 0, 0, 0, 0]
    moedas = [0, 0, 0, 0, 0, 0]
    
    valor = calcula(NOTAS, notas, valor)
    valor = calcula(MOEDAS, moedas, valor)

    return (notas, moedas)

def calcula(monetario, lista, valor):
    for i, moeda in enumerate(monetario):
        while valor >= moeda:
            lista[i] += 1
            valor -= moeda
            valor = round(valor, 2)
    return valor


# A solução abaixo demonstra alguns dos conceitos que
# comentamos no final do dojo e foi adicionada para fins
# didáticos sobre python

def moedas2(valor):
    (notas, valor) = calcula2(valor, NOTAS)
    (moedas, valor) = calcula2(valor, MOEDAS)

    return (notas, moedas)

def calcula2(valor, cedulas):
    quantidades = [0] * len(cedulas)
    for (i, cedula) in enumerate(cedulas):
        # poderíamos usar divmod() também
        quantidades[i] = int(valor / cedula)
        valor = round(valor % cedula, 2)
    return (quantidades, valor)
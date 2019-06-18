def solucao(texto):
    ranges = []
    texto = texto.replace(' ', '')
    texto = list(sorted(set(texto)))
    contexto = []
    while len(texto):
        char = texto.pop(0)
        if not contexto:
            contexto = [char, char]
        elif ord(char) - ord(contexto[-1]) > 1:
            ranges.append(f'{contexto[0]}:{contexto[1]}')
            contexto = [char, char]
        else:
            contexto[1] = char
    
    if contexto:
        ranges.append(f'{contexto[0]}:{contexto[1]}')
        
    return ranges
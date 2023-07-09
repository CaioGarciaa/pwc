
# 1. Reverta a ordem das palavras nas frases, mantendo a ordem das palavras:

def Reverter(x):
    palavra = x.split()
    s = palavra[::-1]
    c = ' '.join(s)
    return c

input = "Hello, World! OpenAI is amazing"
output = Reverter(input)
print(output)

# 2. Remova todos os caracteres duplicados da string abaixo:

def remove_duplicacao(f):
    lista = []
    for j in f:
        if j not in lista:
            lista.append(j)
    return ''.join(lista)

input = "Hello, World!"
output = remove_duplicacao(input)
print(output)

# 3. Encontre a substring palindroma mais longa na string abaixo:


def substring(frase):
    longo = ""
    for i in range(len(frase)):
        for j in range(i+1, len(frase)+1):
            substring = frase[i:j]
            if substring == substring[::-1] and len(substring) > len(longo):
                longo = substring
    return longo

input = "babad"
output = substring(input)
print(output)

# 4. Coloque em maiúscula a primeira letra de cada frase na string

def maiuscula(palavra):
    j = palavra.split('. ')
    lista = []
    for s in j:
        if "?" in s:
            s = s.split('? ')
            f = [sub.capitalize() for sub in s]
            senteca = "? ".join(f)
        else:
            senteca = s.capitalize()
        lista.append(senteca)
    return '. '.join(lista)

input = "hello. how are you? i'm fine, thank you."
output = maiuscula(input)
print(output)

# 5 Ventique se a string é um anagrama de um palindromo

from collections import Counter

def anagrama(palavra):
    j = Counter(palavra)
    frase = 0
    for s in j.values():
        if s % 2 != 0:
            frase += 1
        if frase > 1:
            return False
    return True

input = "racecar"
output = anagrama(input)
print(output)



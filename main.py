import random
from pdflib import gera_pdf

def print_matriz(matriz: list) -> None:
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], ' ', end='')
        print()


def coloca_palavra(mapa: list, palavra: str, sentido='horizontal', modo='normal') -> list:
    linha = len(mapa)
    coluna = len(mapa[0])
    if modo == 'invertido':
        palavra = palavra[::-1]
    if sentido == 'horizontal':
        inicio_min = 0
        inicio_max = coluna - 1 - len(palavra)
        indice = 0
        feito = False
        while feito == False:
            inicio = random.randint(inicio_min, inicio_max)
            i = random.randint(0, linha - 1)
            pode_fixar = True
            for j in range(inicio, inicio + len(palavra)):
                if mapa[i][j] != '*' and mapa[i][j] != palavra[indice]:
                    pode_fixar = False
                indice += 1
            indice = 0
            if pode_fixar == True:
                for j in range(inicio, inicio + len(palavra)):
                    mapa[i][j] = palavra[indice]
                    indice += 1
                feito = True
    elif sentido == 'vertical':
        inicio_min = 0
        inicio_max = linha - 1 - len(palavra)
        indice = 0
        feito = False
        while feito == False:
            inicio = random.randint(inicio_min, inicio_max)
            j = random.randint(0, coluna - 1)
            pode_fixar = True
            for i in range(inicio, inicio + len(palavra)):
                if mapa[i][j] != '*' and mapa[i][j] != palavra[indice]:
                    pode_fixar = False
                indice += 1
            indice = 0
            if pode_fixar == True:
                for i in range(inicio, inicio + len(palavra)):
                    mapa[i][j] = palavra[indice]
                    indice += 1
                feito = True
    elif sentido == 'subindo':
        inicio_min_linha = len(palavra) - 1
        inicio_max_linha = linha - 1
        inicio_min_coluna = 0
        inicio_max_coluna = coluna - len(palavra)
        indice = 0
        feito = False
        while feito == False:
            inicio_linha = random.randint(inicio_min_linha, inicio_max_linha)
            inicio_coluna = random.randint(inicio_min_coluna, inicio_max_coluna)
            pode_fixar = True
            i = inicio_linha
            j = inicio_coluna
            while j < inicio_coluna + len(palavra):
                if mapa[i][j] != '*' and mapa[i][j] != palavra[indice]:
                    pode_fixar = False
                i -= 1
                j += 1
                indice += 1
            indice = 0
            if pode_fixar == True:
                i = inicio_linha
                j = inicio_coluna
                while j < inicio_coluna + len(palavra):
                    mapa[i][j] = palavra[indice]
                    i -= 1
                    j += 1
                    indice += 1
                feito = True
    elif sentido == 'descendo':
        inicio_min_linha = 0
        inicio_max_linha = linha - len(palavra)
        inicio_min_coluna = 0
        inicio_max_coluna = coluna - len(palavra)
        indice = 0
        feito = False
        while feito == False:
            inicio_linha = random.randint(inicio_min_linha, inicio_max_linha)
            inicio_coluna = random.randint(inicio_min_coluna, inicio_max_coluna)
            pode_fixar = True
            i = inicio_linha
            j = inicio_coluna
            while j < inicio_coluna + len(palavra):
                if mapa[i][j] != '*' and mapa[i][j] != palavra[indice]:
                    pode_fixar = False
                i += 1
                j += 1
                indice += 1
            indice = 0
            if pode_fixar == True:
                i = inicio_linha
                j = inicio_coluna
                while j < inicio_coluna + len(palavra):
                    mapa[i][j] = palavra[indice]
                    i += 1
                    j += 1
                    indice += 1
                feito = True
    return mapa


def gera_mapa(linha: int, coluna: int) -> list:
    mapa = []
    for i in range(linha):
        mapa_linha = []
        for j in range(coluna):
            mapa_linha.append('*')
        mapa.append(mapa_linha)
    return mapa

def caca_palavras(palavras: list, linha: int, coluna: int):
    mapa = gera_mapa(linha, coluna)
    sentidos = ['horizontal', 'vertical', 'subindo', 'descendo']
    modos = ['normal', 'invertido']
    for palavra in palavras:
        sentido = sentidos[random.randint(0, len(sentidos) - 1)]
        modo = modos[random.randint(0, len(modos) - 1)]
        mapa = coloca_palavra(mapa, palavra, sentido, modo)
    print_matriz(mapa)
    letras = 'qwertyuiopasdfghjklçzxcvbnm'
    for i in range(linha):
        for j in range(coluna):
            if mapa[i][j] == '*':
                indice = random.randint(0, len(letras) - 1)
                mapa[i][j] = letras[indice]
    return mapa


def to_string(mapa: list) -> str:
    string = ''
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            string += mapa[i][j] + ' '
        string += '\n'
    return string


def to_list(mapa: list) -> list:
    list_mapa = []
    for i in range(len(mapa)):
        string = ''
        for j in range(len(mapa[0])):
            string += str(mapa[i][j]).upper() + ' '
        list_mapa.append(string)
    return list_mapa

linha = 18
coluna = 24

palavras = ['pai','céu','azul','dia','preguiça','amizade','sinais','domingo','vento', 'solidariedade','saudade', 'vida']
if len(palavras) != 12:
    print('Preciso de 12 palavras')
    exit()


mapa = caca_palavras(palavras, linha, coluna)

print('=' * 20)
print_matriz(mapa)

print('-' * 20)
str_mapa = to_string(mapa)
print(str_mapa)

list_mapa = to_list(mapa)

gera_pdf(palavras, list_mapa)

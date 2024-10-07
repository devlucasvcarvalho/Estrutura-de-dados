import random
from collections import Counter

def tem_aniversarios_iguais(aniversarios):
    contador = Counter(aniversarios)
    for count in contador.values():
        if count > 1:
            return True
    return False

def gerar_aniversarios(n):
    return [random.randint(1, 365) for _ in range(n)]

def testar_paradoxo(experimentos=1000):
    resultados = {}
    for n in range(5, 101, 5):
        count_iguais = 0
        for _ in range(experimentos):
            aniversarios = gerar_aniversarios(n)
            if tem_aniversarios_iguais(aniversarios):
                count_iguais += 1
        probabilidade = count_iguais / experimentos
        resultados[n] = probabilidade
    return resultados

# Executar os testes e imprimir os resultados
resultados = testar_paradoxo()
for n, probabilidade in resultados.items():
    print(f"Para n = {n}, a probabilidade de aniversários iguais é {probabilidade:.2f}")

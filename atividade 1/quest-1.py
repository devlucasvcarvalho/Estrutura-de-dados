def encontrar_min_max(numeros):
    if not numeros:
        return None
    menor = min(numeros)
    maior = max(numeros)
    return (menor, maior)

# Exemplo de uso
sequencia = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
resultado = encontrar_min_max(sequencia)
print(f"O menor número é {resultado[0]} e o maior número é {resultado[1]}")
def soma_dos_quadrados_pares(n):
    soma = 0
    for i in range(1, n):
        if i % 2 == 0:
            soma += i ** 2
    return soma

# Exemplo de uso
n = 5
resultado = soma_dos_quadrados_pares(n)
print(f"A soma dos quadrados dos inteiros positivos pares menores que {n} é {resultado}")
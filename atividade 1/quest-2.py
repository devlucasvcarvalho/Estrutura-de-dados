def soma_dos_quadrados(n):
    soma = 0
    for i in range(1, n):
        soma += i ** 2
    return soma

# Exemplo de uso
n = 5
resultado = soma_dos_quadrados(n)
print(f"A soma dos quadrados dos inteiros positivos menores que {n} é {resultado}")
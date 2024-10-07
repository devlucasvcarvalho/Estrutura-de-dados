def todos_diferentes(numeros):
    return len(numeros) == len(set(numeros))

# Exemplo de uso
sequencia = [1, 2, 3, 4, 5]
resultado = todos_diferentes(sequencia)
print(f"Todos os números são diferentes: {resultado}")

sequencia = [1, 2, 3, 4, 5, 5]
resultado = todos_diferentes(sequencia)
print(f"Todos os números são diferentes: {resultado}")
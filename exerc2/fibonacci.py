def fibonacci(n):
    """Gera a sequência de Fibonacci até o maior número igual ou maior que n."""
    a, b = 0, 1
    sequencia = [a, b]
    while b < n:
        a, b = b, a + b
        sequencia.append(b)
    return sequencia


def pertence_fibonacci(numero):
    """Verifica se um número pertence à sequência de Fibonacci."""
    a, b = 0, 1
    while b <= numero:
        if b == numero:
            return True
        a, b = b, a + b
    return False


numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

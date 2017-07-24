def fib(n):
    """Gerador Fibonacci
    Gera qualquer número fib possível

    Args:
        n (int): Número de fibs a serem gerados. Mínimo 2
    Returns:
        fib (int)
    """

    # Python suporta definições simultâneas
    a, b = 0, 1
    # Gera e retorna o primeiro e segundo fibs
    yield a
    yield b
    num = 2
    # Enquanto num < n
    while num < n:
        # Gera o próximo fib em b e salva o anterior em a
        a, b = b, a + b
        # Retorna o próximo fib
        yield b
        # Incrementa num
        num += 1


# Imprime os 10 primeiros fibs na tela
for i in fib(10):
    print(i, end=" ")
# Nova linha pra terminar o programa
print()

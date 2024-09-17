def fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

numero_informado = 34

if fibonacci(numero_informado):
    print(f"O número {numero_informado} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_informado} não pertence à sequência de Fibonacci.")

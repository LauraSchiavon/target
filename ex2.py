def fibonacci(n):
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def verifica_pertence(numero, sequencia):
    if numero in sequencia:
        return True
    else:
        return False

numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

sequencia_fibonacci = fibonacci(numero)
if verifica_pertence(numero, sequencia_fibonacci):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

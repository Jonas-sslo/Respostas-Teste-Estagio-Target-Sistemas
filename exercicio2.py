def isFibonacci(valor):
    if valor < 0:
        print("Esse número não está na série de Fibonacci")
    else:
        a, b = 0, 1
        while a <= valor:
            if a == valor: 
                print(f"O valor {valor} está na série de Fibonacci")
                return 
            a, b = b, a + b
        print(f"O valor {valor} não está na série de Fibonacci")

entrada = int(
    input("Insira um valor para ver se ele está ou não na série de Fibonacci: ")
)
isFibonacci(entrada)
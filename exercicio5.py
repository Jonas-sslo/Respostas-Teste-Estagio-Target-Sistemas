def inverte_palavra(palavra):
    palavra = palavra.replace(" ", "")
    palavra = palavra[::-1]
    print(f"Aqui está a sua palavra invertida: {palavra}")


inverte_palavra("subi no onibus")
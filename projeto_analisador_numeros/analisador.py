def analisar_numeros(numeros):
    total = sum(numeros)
    media = total / len(numeros)
    maior = max(numeros)
    menor = min(numeros)

    print(f"Você digitou {len(numeros)} números.")
    print(f"Soma: {total}")
    print(f"Média: {media:.2f}")
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")

# Programa principal
entrada = input("Digite números separados por vírgula: ")
lista_numeros = [int(num.strip()) for num in entrada.split(",")]

analisar_numeros(lista_numeros)

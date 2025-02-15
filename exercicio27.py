numero_inicial = int(input("Escolha o número inicial: "))
numero_final = int(input("Escolha o número final: "))

par_impar = int(input("Quer números pares [1] ou ímpares [2]: "))

soma = 0  # Definimos a variável soma para armazenar o somatório dos números
 if par_impar == 1:
    print("Os números pares são: ")
elif par_impar == 2:
    print("Os números ímpares são: ")

# Verificação de números pares ou ímpares:
for x in range(numero_inicial, numero_final + 1):  # Faz a contagem de todos os números desde o número inicial ao final
    if par_impar == 1:
        if x % 2 == 0:  # Se o resto da divisão for zero, é par
            print(x, end=" ")
            soma += x  # Vai somando os números aos outros
    elif par_impar == 2:
        if x % 2 != 0:
            print(x, end=" ")
            soma += x  # Vai somando os números uns aos outros
    else:
        print("Opção inválida")
        break

print()
if par_impar == 1:
    print(f"A soma de todos os números pares é {soma}.")
elif par_impar == 2:
    print(f"A soma de todos os números ímpares é {soma}.")


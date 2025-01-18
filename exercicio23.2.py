# solicitando ao usuario que insira o numero inicial
numero_inicial = int(input("Digite o numero inicial: "))

# solicitando ao usuario que insira o numero final
numero_final = int(input("Digite o numero final: "))

# exibindo todos os numeros entre o numero inicial e o numero final (inclusive)
print(f"Os numeros entre [numero inicial] e [numero final] são: ")
for i in range(numero_inicial, numero_final + 1):
    print(i)
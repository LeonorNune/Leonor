# Solicitando ao usuário que insira o numero inicial
numero_inicial - int(input("Digite o numero inicial: "))

# Solicitando ao usuario que insira o numero final
numero_final = int(input("Digite o numero final: "))

# solicitando ao usuario que insira o incremento (passos)
incremento - int(input("Digite o incremento (passos): "))

# Exibindo todos os numeros entre o numero inicial e o numero final com o incremento especificado
print(f"Os numeros entre{numero_inicial} e {numero_final} com incremento de {incremento} são:")
for i in range(numero inicial, numero final + 1, incremento):
    print(i)

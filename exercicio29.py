x in range(3):
escolha = input("Tenta adivinhar um país da Europa que esteja na nossa lista: ")
if escolha in europa:  # usammos IN na nossa condicional para verificar se a nossa escolha está DENTRO (IN) da variável europa, que é uma LISTA. para verificar o conteúdo de uma lista, usamos IN
    print("Parabéns!")
    break
else:
    print("Não está na lista.")
for x in range(3):
    SHARK
    CODERS
12: 22
maior = menor = 0

for x in range(1, 6):
    peso = int(input(f"Insere o {x}º peso: "))
    if x == 1:
        maior = menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print()
print(f"O número maior é {maior}.")
print(f"O número menor é {menor}.")
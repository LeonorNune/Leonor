salario=int(input("Quanto ganhas por mês?:"))
#input onde o utilizador insere o velor numérico para efetuar as contas
diario= salario/30 #conta que determina quanto ganhamos por DIA
hora=diario/8 #já obtivemos o valor que ganhamos por DIA, então dividimos pela quantidade de HORAS DE TRABALHO
# assim chegamos á quantidade de dinheiro que ganhamos por HORA.

print("o seu saldo por hora é de:",hora)
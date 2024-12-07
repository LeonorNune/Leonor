salario=int(input("Quanto recebes por mês?: ")) #este input vai decidir quanto de reajuste vamos receber

reajuste=0 #criamos uma variável vazia para alterar o seu valor de acordo com o salário recebido.

salario_novo=0 #aqui, acontece o mesmo

if salario<=500:
    reajuste=salario*0.15 #cálculo do aumento
    salario_novo=salario+reajuste #cálculo do novo valor

    print("Tens um reajuste de 15%, e o teu salário passa a ser: ",salario_novo,"€.")
elif salario <=1000:
    reajuste=salario*0.10
    salario_novo=salario+reajuste

    print("Tens um reajuste de 10%, e o teu salário passa a ser: ",salario_novo,"€.")
elif salario>1000:
    reajuste=salario*0.05
    salario_novo=salario+reajuste


    print("Tens um reajuste de 5%, e o teu salário passa a ser: ",salário_novo,"€.")
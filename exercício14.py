#-------------IF E ELIF-----------------


#usamos o ELIF para adicionar uma condição á condição principal que foi definida quando os usamos IF
#isto implica que:
#-O ciclo condicional [IF, ELIF, ELSE] funciona em conjunto
#-Se introduzir uma condição (IF), posso adicionar mais condições no mesmo contexto! como por exemplo:

idade_veiculo=int(input("Quantos anos tem o teu veiculo?:")) #primeiro contexto, ou seja, só a idade do veículo
bateria=int(input("A quanto vai a bateria?"))#segundo contexto, ou seja, só a energia que o veiculo tem

#neste caso, a idade e a bateria não têm nada a ver uma com a outra

if idade_veiculo<=10:
    print("O teu carro é seminovo.")
elif idade_veiculo<=5:
    print("O teu carro é novo.")
else:
    print("O teu carro é antigo")
if bateria <=80:
    print("Ainda tens bastante bateria!")
elif bateria <=30:
    print("Estás a ficar com pouca bateria!")
elif bateria<=10:
    print("Carrega-o urgentemente!")
else:
    print("Ainda tens alguma bateria.")

#podemos usar todosos ELIFs que precisarmos de acordo com o propósito do nosso programa.
#no exemplo anterior, quando mudamos a variável sobre a qual se criou a condição, deixamos de usar ELIF e passamos  a usar IF

#-------------CICLOS WHILE E WHILE TRUE------------

#em Python, um ciclo é algo que se repete infinitamente até ter ordem de parar ou uma condição não se verificar

#no ciclo WHILE,temos de indicar a condição que permite que o ciclo continue.
#a cada vez que um ciclo reiniciar, dá-se uma ITERAÇÃO (repetição do ciclo)

#a cada ITERAÇÃO, a condição de um ciclo é novamente avaliada. Quando já não se verificar, o ciclo quebra. (No caso do CICLO WHILE)

#vamos criar um exemplo do ciclo WHILE baseado num cronómetro:

cronómetro= 10 #definimos uma variável que representa o cronómetro com 10 segundos

while cronómetro >= 1: #esta parte do código verifica que o cronómetro se mantém maior ou igual a 1, ou seja, o ciclo só funcionará enquanto cronómetro>=1 bom
Print(cronómetro) #aqui, fazemos print do valor da variável cronómetro a cada iteração
Cronómetro-=1 #subtraímos 1 valor a cada resultado da iteração anterior

Print(“o foguetão está a partir…”) #esta print é realizada PÓS CICLO, ou seja, Quando cronómetro DEIXA DE SER >=1, o ciclo WHILE quebra#no ciclo WHILE TRUE, não precisamos de indicar a condição para que ele continue, porque vai continuar infinitamente até definirmos quando deve parar
#ao contrário do ciclo WHILE, o WHILE TRUE não pára automaticamente, ou saia, a condição para ele parar tem de ser VERIFICADA ou VERDADEIRA
#no ciclo WHILE ISTO não acontece, porque a sua condição tem de DEIXAR DE VERIFICAR para que ele pare.
cronómetro2-=1 #subtraimos 1 valor a cada iteração
If cronómetro2-=1: #INTRODUZIMOS A CONDICAO


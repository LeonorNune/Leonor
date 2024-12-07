instalacao= int(input("""Qual é o teu tipo de instalação? Seleciona um número para prosseguir:

[1] - Residencial

[2] - Comercial

[3] - Industrial: """)) #este input converte os númeors (1, 2, e 3) para o tipo de instalação que temos.
#1 corresponde a instalação residencial
#2 corresponde a instalação comercial
#3 corresponde a instalação industrial

consumo= int(input("Quanta energia (em kWh) consome a tua instalação?: ")) #aqui, indicamos a quantidade de energia que consumimos na nossa instalação.

pagamento=0 #criamos uma variável vazia para armazenar a quantia que vamos pagar DE ACORDO COM AS CONDIÇÕES (vai alterar o seu valor ao longo do código)

#segundo a tabela de valores e tipos de instalação, temos de pagar uma certa quantia mediante a instalação e a energia consumida (consumo)
#isto é feito com CONDICIONAIS e MÚLTIPLAS CONDICIONAIS com AND e OR

if instalacao==1 and consumo<=500:
    pagamento=0.40

    print("Como vives numa instalação RESIDENCIAL [1] e consomes até 500kWh, tens de pagar:", pagamento,"€.")

elif instalacao==1 and consumo >500:
    pagamento=0.65

    print("Como vives numa instalação RESIDENCIAL [1] e consomes mais do que 500kWh, tens de pagar:", pagamento, "€.")

elif instalacao==2 and consumo <=1000:
    pagamento=0.55

    print("Como vives numa instalação COMERCIAL [2] e consomes até 1000kWh, tens de pagar:", pagamento, "€.")
    Partilhar
    Dito
    por
    si:
    elif instalacao == 2 and consumo <= 1000:
    pagamento = 0.55

    print("Como vives numa instalação COMERCIAL [2] e consomes até 1000kWh, tens de pagar:", pagamento, "€.")

elif instalacao == 2 and consumo > 1000:
    pagamento = 0.60

print("Como vives numa instalação COMERCIAL [2] e consomes mais do que 1000kWh, tens de pagar:", pagamento, "€.")
elif instalacao == 3 and consumo <= 5000:
pagamento = 0.55

print("Como vives numa instalação INDUSTRIAL [3] e consomes até 5000kWh, tens de pagar:", pagamento, "€.")

elif instalacao == 3 and consumo > 5000:
pagamento = 0.60

print("Como vives numa instalação INDUSTRIAL [3] e consomes mais do que 5000kWh, tens de pagar:", pagamento, "€.")

else:
print("Tipo inválido, tenta outra vez")

# -------------OUTRA MANEIRA DE REALIZAR O EXERCÍCIO:---------------
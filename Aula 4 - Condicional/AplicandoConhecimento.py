#Faça um programa em Python que, dada a idade de um atleta que será digitada pelo usuário, 
#apresente a mensagem da coluna CATEGORIA de acordo com a tabela abaixo, 
#onde a categoria depende da idade de entrada.

idade = int(input("Idade do Atleta:"))

if idade < 5:
   categoria = "NÃO TEM IDADE PARA SER ATLETA" 
   print(categoria)

elif idade >= 5 and idade <= 7:
   categoria = "INFANTIL A"
   print(categoria)

elif idade >= 8 and idade <= 10 :
   categoria = "INFANTIL B"
   print(categoria)

elif idade >= 11 and idade <= 13 :
   categoria = "JUVENIL A"
   print(categoria)

elif idade >= 14 and idade <= 17 :
   categoria = "JUVENIL B"
   print(categoria)

elif idade >= 18 :
   categoria = "SÊNIOR"
   print(categoria)

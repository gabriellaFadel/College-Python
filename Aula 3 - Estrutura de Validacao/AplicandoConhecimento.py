#Faça um programa em Python para resolver o seguinte problema:  

#O programa deve receber um número inteiro, digitado pelo usuário, e apresentar uma mensagem: 

#- se o número que o usuário digitou for divisível por 3 e por 5 ao mesmo tempo, a mensagem será:
# O número é divisível por 3 e 5. 

#- se o número que o usuário digitou não for divisível por 3 e por 5 ao mesmo tempo, a mensagem será:
# O número não é divisível por 3 e 5. 

valor = int(input())

if ((valor % 3 == 0) and (valor%5 == 0)):
    print("número é divigível por 3 e 5")

else:
    print("O número não é divisível por 3 e 5")

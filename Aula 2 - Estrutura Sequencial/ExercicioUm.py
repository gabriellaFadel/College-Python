# Escreva um programa em Python que permita ao usuário digitar dois números inteiros
# e exibir o resultado para cada uma das seguintes operações:
# soma, subtração, multiplicação, divisão, divisão truncada, resto e exponenciação. 

var1 = int(input("Digite o primeiro valor: "))
var2 = int(input("Digite o segundo valor: "))

#soma
soma = var1+var2
print("A soma dos números digitados é: "+str(soma))

#subtração
subtracao = var1 - var2
print("A subtração dos números digitados é: "+str(subtracao))

#multiplicação
multiplicacao = var1 * var2
print("A multiplicação dos números digitados é: "+str(multiplicacao))

#divisão
divisao = var1 / var2
print("A divisão dos números digitados é: "+str(divisao))

#divisão truncada
divisao_truncada = var1 // var2
print("A divisão dos números digitados é: "+str(divisao_truncada))


#resto
resto = var1 % var2
print("O resto da divisão dos números digitados é: "+str(resto))

#exponenciação

exponenciacao = var1 ** var2
print("O resto da divisão dos números digitados é: "+str(exponenciacao))
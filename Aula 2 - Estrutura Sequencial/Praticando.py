#Faça um programa em Python que receba o custo (valor em reais) de um espetáculo teatral e o preço do convite 
#(valor em reais) desse espetáculo. Esse programa deve calcular e mostrar:  
#a) A quantidade de convites que devem ser vendidos para que, pelo menos, o custo do espetáculo seja alcançado.  
#b) A quantidade de convites que devem ser vendidos para que se tenha um lucro de 23%. 
#Observe que as quantidades calculadas devem ser um número inteiro, portanto, o resultado da quantidade de convites deve ser arredondada para cima, usando a função matemática apropriada em Python. 
import math

custo = float(input("Entre com o custo:"))
convite = float(input("Informe o valor do convite:"))
valor_lucro = custo * 1.23 

convites_custo = math.ceil(custo/convite)
convites_lucro = math.ceil(valor_lucro/convite)

print (int(convites_custo))
print (int(convites_lucro))

#Faça um programa em Python que receba o custo (valor em reais) de um espetáculo teatral e o preço do convite 

#(valor em reais) desse espetáculo. Esse programa deve calcular e mostrar:  

#a) A quantidade de convites que devem ser vendidos para que, pelo menos, o custo do espetáculo seja alcançado.  
#b) A quantidade de convites que devem ser vendidos para que se tenha um lucro de 23%. 

#Observe que as quantidades calculadas devem ser um número inteiro, portanto, o resultado da quantidade de convites deve ser arredondada para cima,
# usando a função matemática apropriada em Python. 

# Aqui você está chamando a biblioteca de matemática, 
#ela vai servir para você acessar métodos matemáticos que existem dentro do python 
import math

# você vai definir as variaveis que recebem o valor em real 
custo = float(input("Entre com o custo:"))
convite = float(input("Informe o valor do convite:"))

# Essa variável serve para definir o valor do lucro dos ingressos 
# É múltiplicado por 1.23 pq precisa ser um lucro de 23% sobre o custo do espetáculo
valor_lucro = custo * 1.23 

#Lembra dos métodos matemáticos que te expliquei, é nesse momento que você vai chamar ele
# math é o nome da biblioteca, e ceil é a funcionalidade dentro dessa biblioteca
# o ceil serve para arredondar para cima 
qtd_convites_custo = math.ceil(custo/convite)
qtd_convites_lucro = math.ceil(valor_lucro/convite)


# E aqui você vai printar a quantidade de convites para cobrir o custo e o lucro do espetáculo
print (int(qtd_convites_custo))
print (int(qtd_convites_custo))

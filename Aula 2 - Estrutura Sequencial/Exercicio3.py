#EXERCÍCIO 3 – Faça um programa em Python que resolva o seguinte problema: 

#Um concurso possui um prêmio no montante de R$ 780.000,00 para dividir entre três ganhadores da seguinte forma: 

#- o primeiro ganhador receberá 46% do prêmio; 

#- o segundo ganhador receberá 32% do prêmio; 

#- o terceiro ganhador receberá o restante do prêmio. 

premio = float(780000.00)

valor_ganhador_1 = float(premio * 0.46)

valor_ganhador_2 = float(premio * 0.32)

valor_ganhador_3 = float(premio - valor_ganhador_1 - valor_ganhador_2)

print (valor_ganhador_1,valor_ganhador_2,valor_ganhador_3)

print("bem-vindo á calculadora")
num1 = float(input("insira o primeiro número:"))
num2 = float(input("insira o segundo número:" ))
operacao= int(input("selecione uma operção (adição = 1, subtração = 2): "))

match operacao :
    case 1:
        soma = num1 + num2
        print(soma)
    case 2:
        subtracao = num1 - num2
        print(subtracao)
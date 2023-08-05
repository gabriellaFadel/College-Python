import Operations

print ("Hello, Wellcome to the Basic Calculator")
print("#######################")
print("Mathematics operations")
print("#######################")
print("1 = addition")
print("2 = subtraction")
print("3 = multiplication")
print("4 = division")
math_operation = int(input("What operation do you want realize?:"))

value_one = int(input("Enter with the first value:"))
value_two = int(input("Enter with the second value:"))

match math_operation:
    case 1:
        Operations.Operations.addition(value_one,value_two)
    case 2:
        Operations.Operations.subtraction(value_one,value_two)
    case 3:
        Operations.Operations.multiplication(value_one,value_two)
    case 4:
        Operations.Operations.division(value_one,value_two)


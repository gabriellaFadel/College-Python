print ("Hello, this is a class with simple mathematics operations")

value_one = int(input("Enter with the first value:"))
value_two = int(input("Enter with the second value:"))

if (value_one <= 0):
    print("the first value must to be bigger than 0")
    value_one = int(input("Please enter with another value:"))

# writer note : if you want concatenete a int variable in python you need convert it for type string, like the exemple 
print("the fisrt value is: "+(str(value_one))+" the second value is: "+(str(value_two))) 

class Operations:

    #Addition
    def addition(val_1,val_2):
        addition = val_1 + val_2
        print("the addition of the first value plus second value is: "+(str(addition)))

    #Subtraction
    def substraction(val_1,val_2):
        substraction = val_1 - val_2
        print("the subtraction of the first value minus second value is: "+(str(substraction)))


    #Multiplication 
    def multiplication(val_1,val_2):
        multiplication  = val_1 * val_2
        print("the multiplication of the first value multiplied by second value is: "+(str(multiplication)))

    #Division 
    def division(val_1,val_2):
        division  = val_1 / val_2
        print("the division of the first value divide by second value is: "+(str(division)))


Operations.addition(value_one,value_two)










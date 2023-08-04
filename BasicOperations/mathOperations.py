print ("Hello, this is a class with simple mathematics operations")

value_one = int(input("Enter with the first value:"))
value_two = int(input("Enter with the second value:"))

if (value_one <= 0):
    print("the first value must to be bigger than 0")
    value_one = int(input("Please enter with another value:"))

# writer note : if you want concatenete a int variable in python you need convert it for type string, like the exemple 
print("the fisrt value is: "+(str(value_one))+" the second value is: "+(str(value_two))) 

#Addition
addition = value_one + value_two
print("the addition of the first value plus second value is: "+(str(addition)))


if(value_one<value_two):
    print("the first value must to be bigger than the second value")
    value_one = int(input("Please enter with a new value:"))

#Subtraction
subtraction = value_one - value_two
print("the subtraction of the first value minus second value is: "+(str(subtraction)))

#Multiplication 
multiplication  = value_one * value_two
print("the multiplication of the first value multiplied by second value is: "+(str(multiplication)))

#Division 
division  = value_one / value_two
print("the division of the first value divide by second value is: "+(str(division)))










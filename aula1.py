print ("Hello, this is a class with simple mathematics operations")

value_one = int(input("Enter with the first value:"))
value_two = int(input("Enter with the second value:"))

if (value_one <= 0):
    print("the first value must to be bigger than 0")
    value_one = int(input("Please enter with another value:"))

# writer note : if you want concatenete a int variable in python you need convert it for type string, like the exemple 

print("the fisrt value is: "+(str(value_one))+" the seconde value is: "+(str(value_two))) 







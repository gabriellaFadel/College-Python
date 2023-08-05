class Operations:

    #Addition
    def addition(val_1,val_2):
        addition = val_1 + val_2
        print("the result of addition is: "+(str(addition)))

    #Subtraction
    def subtraction(val_1,val_2):
        if(val_1 < val_2):
            print("first value must to be bigger than second value")
            val_1 = int(input("Please enter with a new value:"))

        subtraction = val_1 - val_2
        print("the result of subtraction is : "+(str(subtraction)))

    #Multiplication 
    def multiplication(val_1,val_2):
        multiplication  = val_1 * val_2
        print("the result of multiplication is: "+(str(multiplication)))

    #Division 
    def division(val_1,val_2):
        #this  division aways return a result of type integer
        division  = val_1 // val_2
        print("the result of division is:"+(str(division)))

    












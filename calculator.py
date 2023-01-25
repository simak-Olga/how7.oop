class Calculator:
    def add(self, x, y):
        return x+b
    
    def subtract(self, x, y):
        return x-y
        
    def multiply(self, x, y):
        return x*y

    def divide(self,x, y):
        return x/y

#create a calculator object
my_cl = Calculator()

while True:

    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Exit")
    
    ch = int(input("Select operation: "))
    
    #Make sure the user have entered the valid choice
    if ch in (1, 2, 3, 4, 5):
        
        #first check whether user want to exit
        if(ch == 5):
            break
        
        #If not then ask fo the input and call appropiate methods        
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        
        if(ch == 1):
            print(x, "+", y, "=", my_cl.add(x, y))
        elif(ch == 2):
            print(x, "-", y, "=", my_cl.subtract(x, y))
        elif(ch == 3):
            print(x, "*", y, "=", my_cl.multiply(x, y))
        elif(ch == 4):
            print(x, "/", y, "=", my_cl.divide(x, y))
    
    else:
        print("Invalid Input")